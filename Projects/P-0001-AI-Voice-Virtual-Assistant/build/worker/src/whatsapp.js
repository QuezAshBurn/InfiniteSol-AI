// WhatsApp Business Cloud API helpers
// Meta Graph API v18.0

const GRAPH_API = 'https://graph.facebook.com/v18.0';

// SEC-001: HMAC-SHA256 webhook signature verification (X-Hub-Signature-256)
export async function verifySignature(rawBody, sigHeader, appSecret) {
  if (!sigHeader?.startsWith('sha256=')) return false;
  const expected = sigHeader.slice(7); // strip "sha256="

  const enc = new TextEncoder();
  const key = await crypto.subtle.importKey(
    'raw',
    enc.encode(appSecret),
    { name: 'HMAC', hash: 'SHA-256' },
    false,
    ['sign']
  );
  const sig = await crypto.subtle.sign('HMAC', key, rawBody);
  const hex = Array.from(new Uint8Array(sig))
    .map(b => b.toString(16).padStart(2, '0'))
    .join('');

  // Constant-time compare via XOR length check
  if (hex.length !== expected.length) return false;
  let diff = 0;
  for (let i = 0; i < hex.length; i++) diff |= hex.charCodeAt(i) ^ expected.charCodeAt(i);
  return diff === 0;
}

// Fetch media URL from Meta Graph API (audio/ogg)
export async function getMediaUrl(mediaId, accessToken) {
  const res = await fetch(`${GRAPH_API}/${mediaId}`, {
    headers: { Authorization: `Bearer ${accessToken}` },
  });
  if (!res.ok) throw new Error(`Meta media lookup failed: ${res.status}`);
  const data = await res.json();
  return data.url; // expires after ~5 minutes
}

// Download audio bytes (OGG/Opus) from the media URL
export async function downloadMedia(mediaUrl, accessToken) {
  const res = await fetch(mediaUrl, {
    headers: { Authorization: `Bearer ${accessToken}` },
  });
  if (!res.ok) throw new Error(`Media download failed: ${res.status}`);
  return res.arrayBuffer();
}

// Send a text message via WhatsApp Cloud API
export async function sendWhatsApp(toPhone, message, phoneNumberId, accessToken) {
  const res = await fetch(`${GRAPH_API}/${phoneNumberId}/messages`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${accessToken}`,
    },
    body: JSON.stringify({
      messaging_product: 'whatsapp',
      to: toPhone,
      type: 'text',
      text: { body: message },
    }),
  });
  if (!res.ok) {
    const err = await res.text();
    throw new Error(`WhatsApp send failed ${res.status}: ${err}`);
  }
  return res.json();
}
