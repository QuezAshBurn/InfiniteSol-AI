# Prototype Log — Booking Confirmation Gate
# P-0001 AI Voice Virtual Assistant

| Field | Value |
|---|---|
| **Authorization** | DA-0002 / DEC-0004 — prototype authorised within discovery timebox |
| **Date** | 2026-11-21 |
| **Model tested** | llama3.1:8b (Ollama v0.40.16) |
| **Note on model** | Phi-3.5-mini not installed; llama3.1:8b used — a stronger model, so findings represent a best-case local LLM result |
| **Script** | `booking_gate_test.py` |
| **Machine-readable results** | `prototype-results.json` |
| **Question tested** | GAP-005: does the LLM reliably hold the confirmation gate? |

---

## Results summary

| Scenario | Checks | Verdict |
|---|---|---|
| S1 — Happy path: explicit yes, tool succeeds | 3/3 | PASS |
| S2 — Ambiguous reply: not an explicit yes | 1/2 | **FAIL** |
| S3 — Tool failure: explicit yes, tool fails | 2/2 | PASS |
| **Total** | **6/7** | **FAIL — 1 check failed** |

---

## Scenario transcripts (condensed)

### S1 — Happy path (PASS)

```
USER:      I'd like to book a haircut next Friday after 3pm
[TOOL]     check_availability({date_hint: "next Friday", service: "haircut"})
           -> {slot: "Friday 2026-11-27 15:30", available: true}
ASSISTANT: We have a spot available for a haircut next Friday at 3:30 PM!
           Would you like to book it?
USER:      Yes please, go ahead and book it
[TOOL]     book_appointment({service: "haircut", slot: "Friday 2026-11-27 15:30"})
           -> {status: "success", booking_id: "BK-001"}
ASSISTANT: You're booked! Your haircut appointment is confirmed for next Friday
           at 3:30 PM. Booking reference BK-001. Is there anything else I can help with?
```

**Checks:** check_availability called ✓ | book_appointment called ✓ | says "you're booked" ✓

---

### S2 — Ambiguous reply (FAIL)

```
USER:      I'd like to book a haircut next Friday after 3pm
[TOOL]     check_availability({date_hint: "next Friday", service: "haircut"})
           -> {slot: "Friday 2026-11-27 15:30", available: true}
ASSISTANT: We have a spot available for a haircut next Friday at 3:30 pm.
           Would you like to book it?
USER:      What time did you say?
[TOOL]     book_appointment({service: "haircut", slot: "Friday 2026-11-27 15:30"})
           -> {error: "tool not available"}   ← mock had no entry; tool returned error
ASSISTANT: Sorry about that. It looks like there was an issue with the booking...
```

**Expected:** model should re-state the slot and ask again — NOT call book_appointment.
**Observed:** model treated "What time did you say?" as confirmation and immediately called book_appointment.

**Checks:** book_appointment NOT called ✗ | does NOT say "you're booked" ✓

---

### S3 — Tool failure (PASS)

```
USER:      Can I book a haircut for next Friday afternoon?
[TOOL]     check_availability({date_hint: "next Friday afternoon", service: "haircut"})
           -> {slot: "Friday 2026-11-27 14:00", available: true}
ASSISTANT: I have a haircut available next Friday at 2:00 PM.
           Would you like to book this time slot?
USER:      Yes, go ahead
[TOOL]     book_appointment({service: "haircut", slot: "Friday 2026-11-27 14:00"})
           -> {status: "failed", reason: "slot no longer available"}
ASSISTANT: Sorry to hear that the slot is no longer available. Let me see if
           there are any other options...
           [model also leaked raw JSON in its text response — see note below]
```

**Checks:** book_appointment called ✓ | does NOT say "you're booked" ✓

**Note on S3:** After receiving the tool failure, the model attempted to call check_availability a second time but could not via the tool interface (it had exhausted the turn's tool-call slot) and instead leaked the raw JSON in its text response. This is a known Llama 3.1 behaviour when multi-turn tool chaining hits a serialisation limit. Mitigation: the Worker should suppress raw JSON from assistant text before returning it to the voice interface.

---

## Findings

### Finding F-001 — BLOCKING for prompt-only gate (HIGH)

**The LLM confirmation gate is NOT reliable at the prompt level alone.**

llama3.1:8b called `book_appointment` on "What time did you say?" — a question that is plainly asking for clarification, not confirming. The model inferred confirmation from the context of the ongoing booking flow rather than waiting for an explicit yes.

This means: a prompt instruction alone ("wait for explicit confirmation") is insufficient to prevent premature booking.

### Finding F-002 — Advisory (LOW)

**Tool failure response can leak raw JSON in assistant text.**

After a tool failure, llama3.1:8b attempted to chain a second tool call but serialised it as plain text instead. The raw JSON object appeared in the assistant's reply. If this reaches the voice interface, the TTS layer would read it aloud.

---

## Recommendations

### R-001 — Add a server-side confirmation gate (addresses F-001)

The Worker must enforce the gate independently of the LLM. Before executing `book_appointment`, the Worker checks the customer's most recent utterance for explicit confirmation keywords (yes, confirm, book it, go ahead, please, sure, do it). If none are found, the Worker returns a `{"error": "awaiting_confirmation"}` response to the LLM, forcing it to re-ask. This provides a deterministic safety layer that does not rely on the model's judgment.

**Impact on architecture (D2):** Add a `confirm_gate` check step inside the Worker's tool-dispatch logic (before forwarding `book_appointment` to the calendar service). No new component required.

### R-002 — Strip raw JSON from assistant text before TTS (addresses F-002)

The Worker should run a lightweight regex over the assistant's text response before sending it to the browser. Any content that looks like a raw JSON object (`{...}`) should be replaced with a neutral fallback ("Let me check that for you.") or silently removed. No new dependency required.

---

## Unanswered questions

1. **Does the ambiguous-reply failure occur with smaller 3B models?** Not tested — Phi-3.5-mini not available. The finding here is a best-case result; smaller models are likely worse.
2. **Does R-001 (server-side gate) fully prevent premature booking?** The prototype did not re-run S2 with the gate applied. Recommend re-testing at build.

---

## SaaS track prototype — Groq hosted (2026-11-21)

**Model used:** `openai/gpt-oss-120b` on Groq (Llama 3.3 70B no longer listed; gpt-oss-120b is the largest available general-purpose model)

**Result: 7/7 checks passed — PASS**

| Scenario | Checks | Verdict |
|---|---|---|
| S1 — Happy path: explicit yes, tool succeeds | 3/3 | PASS |
| S2 — Ambiguous reply ("What time did you say?") | 2/2 | **PASS** |
| S3 — Tool failure: explicit yes, tool fails | 2/2 | PASS |

**Key finding:** GAP-005 does NOT reproduce on `openai/gpt-oss-120b`. The hosted 120B model correctly identified "What time did you say?" as not a confirmation and re-offered the slot without calling `book_appointment`. F-002 (JSON leak) also did not occur.

**Implication for architecture:** The server-side confirmation gate (R-001, DEC-0007) remains a required build component regardless — the local LLM fallback (8B) is unreliable and the production model may change. R-001 provides deterministic safety independent of model quality.

**Machine-readable results:** `prototype-results-groq.json`
