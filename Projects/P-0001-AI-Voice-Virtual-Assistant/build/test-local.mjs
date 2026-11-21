// Local end-to-end test harness — P-0001
// Sends signed text-type WhatsApp webhook payloads to wrangler dev.
// Requires: wrangler dev running on port 8787 with TEST_MODE=true
// Run: node build/test-local.mjs

import crypto from 'node:crypto';

const BASE = 'http://localhost:8787';
const APP_SECRET = 'local-test-secret'; // must match .dev.vars WHATSAPP_APP_SECRET
const TENANT_T1_NUMBER = '61400000001';  // Aria — Riverside Hair Studio
const CUSTOMER_PHONE   = '61499999001'; // synthetic customer

// ── helpers ──────────────────────────────────────────────────────────────────

function makePayload(displayPhone, customerPhone, text) {
  return {
    object: 'whatsapp_business_account',
    entry: [{
      changes: [{
        value: {
          metadata: { display_phone_number: displayPhone, phone_number_id: displayPhone },
          messages: [{
            from: customerPhone,
            type: 'text',
            text: { body: text },
          }],
        },
      }],
    }],
  };
}

async function send(displayPhone, customerPhone, text) {
  const body = JSON.stringify(makePayload(displayPhone, customerPhone, text));
  const sig = 'sha256=' + crypto.createHmac('sha256', APP_SECRET).update(body).digest('hex');
  const res = await fetch(`${BASE}/webhook`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-hub-signature-256': sig,
    },
    body,
  });
  const json = await res.json().catch(() => ({}));
  return { status: res.status, reply: json.reply ?? '(no reply)' };
}

async function verifyWebhook() {
  const res = await fetch(
    `${BASE}/webhook?hub.mode=subscribe&hub.verify_token=local-verify-token&hub.challenge=abc123`
  );
  return { status: res.status, body: await res.text() };
}

// ── scenarios ────────────────────────────────────────────────────────────────

let pass = 0, fail = 0;

function check(label, condition, got) {
  if (condition) { console.log(`  ✓  ${label}`); pass++; }
  else           { console.error(`  ✗  ${label}\n     got: ${got}`); fail++; }
}

console.log('\n── E-000  Webhook GET verification ──────────────────────────────');
const v = await verifyWebhook();
check('Returns 200', v.status === 200);
check('Echoes challenge', v.body === 'abc123', v.body);

console.log('\n── E-001a  INTRODUCTION — first message ─────────────────────────');
const r1 = await send(TENANT_T1_NUMBER, CUSTOMER_PHONE, 'Hello');
console.log(`  reply: ${r1.reply}`);
check('200 OK', r1.status === 200);
check('Mentions VA name or business', /aria|riverside/i.test(r1.reply), r1.reply);

console.log('\n── E-001b  MENU_PROMPT — booking intent ─────────────────────────');
const r2 = await send(TENANT_T1_NUMBER, CUSTOMER_PHONE, 'I want to book a haircut');
console.log(`  reply: ${r2.reply}`);
check('200 OK', r2.status === 200);
check('Mentions haircut or slot', /haircut|slot|monday|tuesday|wednesday|thursday|friday|saturday|sunday|november|9.00|10.00|am|pm/i.test(r2.reply), r2.reply);

console.log('\n── E-002  R-001 gate — ambiguous reply must NOT book ────────────');
const r3 = await send(TENANT_T1_NUMBER, CUSTOMER_PHONE, 'maybe, what time was that again?');
console.log(`  reply: ${r3.reply}`);
check('200 OK', r3.status === 200);
check('Re-states slot (not confirmed)', !/you.re (all set|booked|confirmed)/i.test(r3.reply), r3.reply);

console.log('\n── E-002b  R-001 gate — explicit yes must proceed ───────────────');
const r4 = await send(TENANT_T1_NUMBER, CUSTOMER_PHONE, 'yes please book it');
console.log(`  reply: ${r4.reply}`);
check('200 OK', r4.status === 200);
// Either confirmed (tool succeeded) or re-ask (slot already taken in this run is fine)
check('Not stuck in gate loop', r4.reply.length > 10, r4.reply);

console.log('\n── E-006  RAG — service info question ───────────────────────────');
const ragPhone = '61499999002'; // fresh customer — new session
const r5 = await send(TENANT_T1_NUMBER, ragPhone, 'Where are you located and what are your hours?');
console.log(`  reply: ${r5.reply}`);
check('200 OK', r5.status === 200);
check('Mentions location or hours', /river|9am|6pm|open|mon|sat|park/i.test(r5.reply), r5.reply);

console.log('\n── E-005  HUMAN_HANDOFF ─────────────────────────────────────────');
const handoffPhone = '61499999003';
await send(TENANT_T1_NUMBER, handoffPhone, 'I need to speak to a person');
const r6 = await send(TENANT_T1_NUMBER, handoffPhone, 'test@example.com');
console.log(`  reply: ${r6.reply}`);
check('200 OK', r6.status === 200);
check('Asks for or confirms contact', /phone|contact|email|noted|follow/i.test(r6.reply), r6.reply);

console.log('\n── E-007  Tenant isolation — wrong number returns silently ──────');
const r7 = await send('61400099999', CUSTOMER_PHONE, 'hello'); // unknown tenant number
check('200 OK (silent reject)', r7.status === 200);

console.log(`\n${'─'.repeat(60)}`);
console.log(`  ${pass} passed  ${fail > 0 ? fail + ' FAILED' : '0 failed'}`);
if (fail > 0) process.exit(1);
