// P-0001 AI Voice Virtual Assistant — Cloudflare Worker entry point
// WhatsApp Business Cloud API → Groq Whisper → Groq LLM → WhatsApp text reply

import { gateBooking, stripJson } from './gate.js';
import { callLLM } from './llm.js';
import { checkAvailability, bookAppointment, recordHandoff } from './tools.js';
import { verifySignature, getMediaUrl, downloadMedia, sendWhatsApp } from './whatsapp.js';

const GROQ_WHISPER_URL = 'https://api.groq.com/openai/v1/audio/transcriptions';
const SESSION_TTL = 3600; // 1 hour

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Meta webhook verification (GET)
    if (request.method === 'GET' && url.pathname === '/webhook') {
      const mode = url.searchParams.get('hub.mode');
      const token = url.searchParams.get('hub.verify_token');
      const challenge = url.searchParams.get('hub.challenge');
      if (mode === 'subscribe' && token === env.WHATSAPP_VERIFY_TOKEN) {
        return new Response(challenge, { status: 200 });
      }
      return new Response('Forbidden', { status: 403 });
    }

    if (request.method === 'POST' && url.pathname === '/webhook') {
      return handleWebhook(request, env);
    }

    return new Response('Not found', { status: 404 });
  },
};

async function handleWebhook(request, env) {
  const rawBody = await request.arrayBuffer();

  // SEC-001: verify Meta HMAC-SHA256 signature
  const sig = request.headers.get('x-hub-signature-256') ?? '';
  if (!await verifySignature(rawBody, sig, env.WHATSAPP_APP_SECRET)) {
    console.error('Signature mismatch');
    return new Response('Forbidden', { status: 403 });
  }

  let payload;
  try {
    payload = JSON.parse(new TextDecoder().decode(rawBody));
  } catch {
    return new Response('Bad request', { status: 400 });
  }

  // Meta sends a "statuses" event for delivery receipts — ignore them
  const entry = payload?.entry?.[0];
  const change = entry?.changes?.[0];
  const value = change?.value;
  const messages = value?.messages;
  if (!messages?.length) return new Response('OK', { status: 200 });

  const msg = messages[0];
  const customerPhone = msg.from;
  const recipientNumber = value?.metadata?.display_phone_number;

  // SEC-001: resolve tenant from recipient WhatsApp number
  const tenant = await loadTenant(recipientNumber, env.DB);
  if (!tenant) {
    console.error(`No tenant for WhatsApp number: ${recipientNumber}`);
    return new Response('OK', { status: 200 }); // hard-stop silently (SEC-001)
  }

  // Load or create session (KV key = tenant_id:customer_phone — SEC-005)
  const sessionKey = `${tenant.tenant_id}:${customerPhone}`;
  const rawSession = await env.KV.get(sessionKey);
  const session = rawSession ? JSON.parse(rawSession) : { messages: [], language: tenant.language_default };

  // Transcribe audio or use text message
  let transcript, language;
  if (msg.type === 'audio') {
    try {
      const mediaUrl = await getMediaUrl(msg.audio.id, env.WHATSAPP_ACCESS_TOKEN);
      const audioBuffer = await downloadMedia(mediaUrl, env.WHATSAPP_ACCESS_TOKEN);
      ({ transcript, language } = await transcribeAudio(audioBuffer, env.GROQ_API_KEY));
    } catch (err) {
      console.error('Transcription error:', err);
      await sendWhatsApp(customerPhone, 'Sorry, I had trouble hearing that. Could you send it again?', tenant.phone_number_id, env.WHATSAPP_ACCESS_TOKEN);
      return new Response('OK', { status: 200 });
    }
  } else if (msg.type === 'text') {
    transcript = msg.text.body;
    language = session.language;
  } else {
    // Unsupported message type (image, sticker, etc.)
    await sendWhatsApp(customerPhone, 'I can only understand text and voice messages. How can I help you?', tenant.phone_number_id, env.WHATSAPP_ACCESS_TOKEN);
    return new Response('OK', { status: 200 });
  }

  // Persist detected language in session
  if (language) session.language = language;

  // Append customer message to history
  session.messages.push({ role: 'user', content: transcript });

  // Load knowledge base for RAG context injection
  const ragContext = await loadRagContext(tenant.tenant_id, env.DB);

  // LLM chat loop (tool calls resolved in-process)
  const reply = await runLLMLoop(session, tenant, language ?? session.language, ragContext, customerPhone, env);

  // R-002: strip JSON bleed before sending
  const cleanReply = stripJson(reply);

  // Send WhatsApp text reply (ponytail: TEST_MODE skips Meta call, returns reply as JSON)
  if (env.TEST_MODE === 'true') {
    session.messages.push({ role: 'assistant', content: cleanReply });
    await env.KV.put(sessionKey, JSON.stringify(session), { expirationTtl: SESSION_TTL });
    return new Response(JSON.stringify({ reply: cleanReply }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  await sendWhatsApp(customerPhone, cleanReply, tenant.phone_number_id, env.WHATSAPP_ACCESS_TOKEN);

  // Append assistant reply and persist session
  session.messages.push({ role: 'assistant', content: cleanReply });
  await env.KV.put(sessionKey, JSON.stringify(session), { expirationTtl: SESSION_TTL });

  return new Response('OK', { status: 200 });
}

// Run LLM + tool execution loop; returns final text reply
async function runLLMLoop(session, tenant, language, ragContext, customerPhone, env) {
  const messages = [...session.messages];
  const lastUserMsg = messages.at(-1)?.content ?? '';

  for (let i = 0; i < 5; i++) { // ponytail: max 5 iterations prevents runaway loops
    const assistantMsg = await callLLM(messages, tenant, language, ragContext, env.GROQ_API_KEY);
    messages.push(assistantMsg);

    if (!assistantMsg.tool_calls?.length) {
      return assistantMsg.content ?? '';
    }

    // Execute each tool call
    const toolResults = [];
    for (const tc of assistantMsg.tool_calls) {
      const args = JSON.parse(tc.function.arguments);
      let result;

      if (tc.function.name === 'check_availability') {
        result = await checkAvailability(args, tenant.tenant_id, env.DB);

      } else if (tc.function.name === 'book_appointment') {
        // R-001: worker-level confirmation gate (DEC-0007)
        if (!gateBooking(lastUserMsg)) {
          result = { status: 'blocked', reason: 'Customer has not explicitly confirmed. Re-present the slot and ask again.' };
        } else {
          result = await bookAppointment(args, tenant.tenant_id, customerPhone, env.DB);
        }

      } else if (tc.function.name === 'record_handoff') {
        const requestId = await recordHandoff(
          tenant.tenant_id, customerPhone,
          args.customer_email, args.reason, env.DB
        );
        result = { status: 'recorded', request_id: requestId };

      } else {
        result = { error: `Unknown tool: ${tc.function.name}` };
      }

      toolResults.push({
        role: 'tool',
        tool_call_id: tc.id,
        content: JSON.stringify(result),
      });
    }

    messages.push(...toolResults);
  }

  return 'Sorry, I ran into an issue. Please try again.';
}

// Load tenant record + services from D1
async function loadTenant(whatsappNumber, db) {
  const tenant = await db.prepare(
    'SELECT tenant_id, name, va_name, whatsapp_number, language_default FROM tenants WHERE whatsapp_number = ?'
  ).bind(whatsappNumber).first();

  if (!tenant) return null;

  // Attach phone_number_id (same as the number in Meta's numbering — set at deploy)
  tenant.phone_number_id = tenant.whatsapp_number;

  const { results: services } = await db.prepare(
    'SELECT name, duration_minutes, price_aud FROM services WHERE tenant_id = ?'
  ).bind(tenant.tenant_id).all();

  tenant.services = services;
  return tenant;
}

// Concatenate all knowledge_sources for a tenant as a single text block
async function loadRagContext(tenantId, db) {
  const { results } = await db.prepare(
    'SELECT title, content FROM knowledge_sources WHERE tenant_id = ? ORDER BY source_id'
  ).bind(tenantId).all();
  return results.map(r => `### ${r.title}\n${r.content}`).join('\n\n');
}

// Groq Whisper STT — returns { transcript, language }
async function transcribeAudio(audioBuffer, apiKey) {
  const form = new FormData();
  form.append('file', new Blob([audioBuffer], { type: 'audio/ogg' }), 'audio.ogg');
  form.append('model', 'whisper-large-v3-turbo');
  form.append('response_format', 'verbose_json'); // returns text + language

  const res = await fetch(GROQ_WHISPER_URL, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${apiKey}`,
      'User-Agent': 'infinitesol-va/1.0',
    },
    body: form,
  });

  if (!res.ok) {
    const err = await res.text();
    throw new Error(`Whisper error ${res.status}: ${err}`);
  }

  const data = await res.json();
  return { transcript: data.text, language: data.language };
}
