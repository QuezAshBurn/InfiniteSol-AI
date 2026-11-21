// Groq LLM dialogue module
// Model: openai/gpt-oss-120b (re-confirm at build — DEC-0004 build note)

const GROQ_URL = 'https://api.groq.com/openai/v1/chat/completions';
const MODEL = 'openai/gpt-oss-120b';

const TOOLS = [
  {
    type: 'function',
    function: {
      name: 'check_availability',
      description: 'Check available appointment slots for a service. Use this when the customer wants to book or find the next available time.',
      parameters: {
        type: 'object',
        properties: {
          service_name: {
            type: 'string',
            description: 'The name of the service (e.g. "Haircut", "Colour", "Initial Assessment")',
          },
          preferred_date: {
            type: 'string',
            description: 'Preferred date in YYYY-MM-DD format. Omit to find the next available slot.',
          },
        },
        required: ['service_name'],
      },
    },
  },
  {
    type: 'function',
    function: {
      name: 'book_appointment',
      description: 'Book an appointment. ONLY call this after the customer has given explicit confirmation (yes, confirm, go ahead, etc.).',
      parameters: {
        type: 'object',
        properties: {
          slot_id: {
            type: 'string',
            description: 'The slot_id returned by check_availability',
          },
          service_name: {
            type: 'string',
            description: 'The service being booked',
          },
        },
        required: ['slot_id', 'service_name'],
      },
    },
  },
];

function buildSystemPrompt(tenant, language, ragContext) {
  const servicesText = (tenant.services || [])
    .map(s => `- ${s.name} (${s.duration_minutes} min${s.price_aud ? ', AUD ' + s.price_aud : ''})`)
    .join('\n');

  return `You are ${tenant.va_name}, a friendly voice assistant from ${tenant.name}. You help customers schedule appointments via WhatsApp text messages.

LANGUAGE: Respond in ${language}. Always match the customer's language throughout the whole conversation.

TONE: Warm, hospitable, and jolly. If the customer is frustrated or upset, stay calm, acknowledge their feelings, and gently help them.

## HOW TO START
When starting a new conversation, introduce yourself: "Hi, this is ${tenant.va_name} from ${tenant.name}, your Voice Assistant, how can I help you?" Then offer these options in a natural, conversational way:
1. Book an appointment
2. Find the next available time
3. Learn about our services
4. Other enquiries

## BOOKING FLOW
1. Find out which service and preferred date/time the customer wants.
2. Call check_availability to find an available slot.
3. Present the slot clearly: service, date, time.
4. Ask if the customer would like to book that slot.
5. Wait for explicit confirmation BEFORE calling book_appointment.
6. Only call book_appointment after the customer clearly says yes, confirms, or accepts.

## CRITICAL RULES
- NEVER say "you're booked", "booking confirmed", or anything implying success UNTIL book_appointment returns {"status": "success"}.
- If the customer's reply is ambiguous ("what time?", "maybe", "I think so"): re-state the slot and ask again. Do NOT call book_appointment.
- If book_appointment fails: immediately call check_availability to find the next available slot and offer it — do not make the customer ask.
- SUGGEST SCHEDULE: when the customer wants the next available time, call check_availability without a preferred_date to find the earliest slot.

## BOOKING CONFIRMATION
When book_appointment returns {"status": "success"}, your reply MUST include ALL of these:
1. Confirmation the booking is done.
2. "Your booking reference is [booking_id]" — use the exact booking_id value from the tool result.
3. "Add to your calendar: [calendar_url]" — use the exact calendar_url value from the tool result.

## HUMAN HANDOFF
If you cannot help or the customer requests a human: tell them you will get back to them. Ask for their email address and phone number. Confirm you have noted it and that the team will follow up. Include "Your reference is [request_id]" using the exact request_id from the record_handoff result. End the booking flow gracefully.

## SERVICES
${servicesText}

## KNOWLEDGE BASE
${ragContext || 'No additional information available. Answer questions about services and hours from the SERVICES list above.'}`;
}

export async function callLLM(messages, tenant, language, ragContext, apiKey) {
  const body = JSON.stringify({
    model: MODEL,
    messages: [
      { role: 'system', content: buildSystemPrompt(tenant, language, ragContext) },
      ...messages,
    ],
    tools: TOOLS,
    tool_choice: 'auto',
    stream: false,
  });

  const res = await fetch(GROQ_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${apiKey}`,
      'User-Agent': 'infinitesol-va/1.0',
    },
    body,
  });

  if (!res.ok) {
    const err = await res.text();
    throw new Error(`Groq LLM error ${res.status}: ${err}`);
  }

  const data = await res.json();
  return data.choices[0].message;
}
