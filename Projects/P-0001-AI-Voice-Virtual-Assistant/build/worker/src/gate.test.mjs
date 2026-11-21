// gate.test.mjs — R-001 confirmation gate tests
// Run: node --experimental-vm-modules build/worker/src/gate.test.mjs
// (or: node build/worker/src/gate.test.mjs from project root)

import assert from 'node:assert/strict';
import { gateBooking, stripJson } from './gate.js';

let pass = 0;
let fail = 0;

function ok(label, result, expected = true) {
  if (result === expected) {
    console.log(`  ✓  ${label}`);
    pass++;
  } else {
    console.error(`  ✗  ${label}  (got ${result}, expected ${expected})`);
    fail++;
  }
}

// ── English ──────────────────────────────────────────────────────────────────
console.log('\nEnglish confirmations');
ok('yes',          gateBooking('yes'));
ok('Yeah go ahead', gateBooking('Yeah go ahead'));
ok('ok',           gateBooking('ok'));
ok('sure',         gateBooking('sure'));
ok('sounds good',  gateBooking('sounds good'));

console.log('\nEnglish rejections (must NOT pass gate)');
ok('no',           gateBooking('no'),           false);
ok('cancel',       gateBooking('cancel'),        false);
ok('never mind',   gateBooking('never mind'),    false);
ok('maybe later',  gateBooking('maybe later'),   false);

// ── Filipino / Tagalog ────────────────────────────────────────────────────────
console.log('\nFilipino / Tagalog confirmations');
ok('oo (standalone)',   gateBooking('oo'));
ok('Oo naman',         gateBooking('Oo naman'));
ok('opo',              gateBooking('opo'));
ok('sige',             gateBooking('sige'));
ok('ayos',             gateBooking('ayos'));

console.log('\nFilipino false-positive guard');
// ponytail: these are the exact substring traps the word-boundary fix closes
ok('"noong" must NOT match "oo"',    gateBooking('noong isang linggo'),  false);
ok('"siguro" must NOT match "sige"', gateBooking('siguro bukas'),        false);

// ── Spanish ──────────────────────────────────────────────────────────────────
console.log('\nSpanish confirmations');
ok('sí',       gateBooking('sí'));
ok('claro',    gateBooking('claro'));
ok('dale',     gateBooking('dale'));

// ── French ───────────────────────────────────────────────────────────────────
console.log('\nFrench confirmations');
ok('oui',      gateBooking('oui'));
ok("d'accord", gateBooking("d'accord"));

// ── Indonesian / Malay ────────────────────────────────────────────────────────
console.log('\nIndonesian / Malay confirmations');
ok('iya',    gateBooking('iya'));
ok('boleh',  gateBooking('boleh'));
ok('oke',    gateBooking('oke'));
ok('setuju', gateBooking('setuju'));

// ── Portuguese ───────────────────────────────────────────────────────────────
console.log('\nPortuguese confirmations');
ok('sim',      gateBooking('sim'));

console.log('\nPortuguese false-positive guard');
ok('"similar" must NOT match "sim"', gateBooking('that is similar to what I want'), false);

// ── German ───────────────────────────────────────────────────────────────────
console.log('\nGerman confirmations');
ok('ja',    gateBooking('ja'));
ok('genau', gateBooking('genau'));

console.log('\nGerman false-positive guard');
ok('"japanese" must NOT match "ja"', gateBooking('japanese food'), false);

// ── East Asian / Unicode ──────────────────────────────────────────────────────
console.log('\nUnicode confirmations');
ok('はい (Japanese)',  gateBooking('はい'));
ok('네 (Korean)',     gateBooking('네'));
ok('好的 (Chinese)',  gateBooking('好的'));
ok('نعم (Arabic)',    gateBooking('نعم'));
ok('हाँ (Hindi)',     gateBooking('हाँ'));
ok('ใช่ (Thai)',      gateBooking('ใช่'));

// ── R-002 stripJson ───────────────────────────────────────────────────────────
console.log('\nstripJson (R-002)');
ok('strips ```json``` block',
  stripJson('Here you go\n```json\n{"status":"ok"}\n```\nAll done.'),
  'Here you go\n\nAll done.');
ok('strips bare JSON object line',
  stripJson('Got it.\n{"slot_id":1,"status":"success"}\nSee you then!').includes('{'),
  false);
ok('leaves plain text alone',
  stripJson('You are all set!'),
  'You are all set!');

// ── Summary ───────────────────────────────────────────────────────────────────
console.log(`\n${'─'.repeat(50)}`);
console.log(`  ${pass} passed  ${fail > 0 ? fail + ' FAILED' : '0 failed'}`);
if (fail > 0) process.exit(1);
