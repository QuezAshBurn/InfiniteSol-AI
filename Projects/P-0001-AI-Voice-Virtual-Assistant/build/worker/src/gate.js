// R-001: server-side confirmation gate (DEC-0007)
// Worker checks the customer's last utterance before forwarding book_appointment.
// Prompt-level gate alone is unreliable on smaller models (PROTOTYPE-LOG F-001).
// Multilingual keywords added for DEC-0012 multi-language support (fix OQ-D8-001).

const CONFIRM_KEYWORDS = [
  // English
  'yes', 'confirm', 'book it', 'go ahead', 'please', 'sure', 'do it',
  'yep', 'yeah', 'ok', 'okay', 'correct', 'that one', 'sounds good',
  'perfect', 'great', 'definitely', 'absolutely',
  // Filipino / Tagalog
  'oo', 'oo naman', 'opo', 'sige', 'ayos', 'tuloy',
  // Spanish
  'sí', 'claro', 'dale', 'de acuerdo',
  // French
  'oui', "d'accord", 'bien sûr',
  // Indonesian / Malay
  'iya', 'boleh', 'oke', 'setuju',
  // Portuguese
  'sim', 'pode ser',
  // German
  'ja', 'genau', 'in ordnung',
  // Italian
  'sì', 'certo', 'va bene',
  // Vietnamese
  'vâng', 'đồng ý', 'được',
  // Japanese
  'はい', 'いいですよ', 'お願いします',
  // Korean
  '네', '예', '좋아요', '확인',
  // Thai
  'ใช่', 'โอเค', 'ตกลง',
  // Arabic
  'نعم', 'تمام', 'موافق',
  // Hindi
  'हाँ', 'हां', 'ठीक है',
  // Chinese
  '好的', '确认', '可以',
];

// ponytail: lookbehind/lookahead instead of \b for Latin/Latin-extended single words.
// \b treats accented chars (í, ì, â …) as \W so \bsí\b never fires after the accent.
// Negative lookaround on the full Latin+Extended range catches word boundaries correctly.
// Phrases (space) and non-Latin scripts (CJK, Arabic, Devanagari, Thai) use includes().
const _LATIN = '[a-zA-ZÀ-ɏḀ-ỿ]';
function matchesKeyword(text, kw) {
  if (new RegExp(`^${_LATIN}+$`).test(kw)) {
    return new RegExp(`(?<!${_LATIN})${kw}(?!${_LATIN})`, 'iu').test(text);
  }
  return text.includes(kw);
}

export function gateBooking(text) {
  const lower = text.toLowerCase();
  return CONFIRM_KEYWORDS.some(kw => matchesKeyword(lower, kw.toLowerCase()));
}

// R-002: strip raw JSON bleed from assistant text before sending to customer
export function stripJson(text) {
  // Remove ```json ... ``` blocks
  text = text.replace(/```json[\s\S]*?```/gi, '');
  // Remove bare { ... } or [ ... ] spanning multiple lines
  text = text.replace(/^\s*[\[{][\s\S]*?[\]}]\s*$/gm, '');
  return text.trim();
}
