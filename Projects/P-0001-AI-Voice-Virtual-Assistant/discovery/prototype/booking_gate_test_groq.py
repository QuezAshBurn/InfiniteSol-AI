#!/usr/bin/env python3
"""
Booking confirmation gate prototype — Groq hosted LLM
Same 3 scenarios as booking_gate_test.py; uses Groq OpenAI-compatible API.
Reads GROQ_API_KEY from environment.
"""
import io, json, os, sys, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL     = "openai/gpt-oss-120b"
API_KEY   = os.environ.get("GROQ_API_KEY", "")

if not API_KEY:
    print("ERROR: set GROQ_API_KEY environment variable before running")
    sys.exit(1)

SYSTEM = """\
You are a voice assistant for appointment scheduling. Be hospitable, respectful, and jolly.
Stay calm and helpful if a customer is frustrated or a booking fails.

BOOKING RULES - follow exactly:
1. Use check_availability to find an open slot before offering anything.
2. Offer the slot clearly: state the date, time, and service.
3. Wait for EXPLICIT confirmation ("yes", "confirm", "book it", "go ahead") before calling book_appointment.
   - Ambiguous replies ("what time?", "maybe", "how long?", "is that right?") are NOT confirmation.
   - If the reply is ambiguous, re-offer the slot and ask again. Do not call book_appointment yet.
4. Only say "you're booked" (or equivalent) after book_appointment returns {"status": "success"}.
5. If book_appointment returns {"status": "failed"}, apologise, do NOT say "you're booked",
   and offer to try another slot or connect the customer to a person.
"""

TOOLS = [
    {"type": "function", "function": {
        "name": "check_availability",
        "description": "Check available appointment slots for a service on a given date.",
        "parameters": {
            "type": "object",
            "properties": {
                "service":   {"type": "string", "description": "The service requested, e.g. haircut"},
                "date_hint": {"type": "string", "description": "Preferred date, e.g. 'next Friday'"}
            },
            "required": ["service"]
        }
    }},
    {"type": "function", "function": {
        "name": "book_appointment",
        "description": "Book the offered slot. Only call this after the customer explicitly confirms.",
        "parameters": {
            "type": "object",
            "properties": {
                "service": {"type": "string"},
                "slot":    {"type": "string", "description": "The exact slot string returned by check_availability"}
            },
            "required": ["service", "slot"]
        }
    }}
]


def call_groq(messages):
    body = json.dumps({
        "model": MODEL,
        "messages": messages,
        "tools": TOOLS,
        "tool_choice": "auto",
        "stream": False
    }).encode()
    req = urllib.request.Request(
        GROQ_URL, data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
            "User-Agent": "python-groq-prototype/1.0",
        }
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read())
    return data["choices"][0]["message"]


def run_scenario(turns, mock_results):
    msgs   = [{"role": "system", "content": SYSTEM}]
    called = []

    for user_text in turns:
        msgs.append({"role": "user", "content": user_text})
        print(f"  USER:      {user_text}")

        while True:
            m = call_groq(msgs)
            # Groq returns tool_calls as a list; content may be null
            tool_calls = m.get("tool_calls") or []
            if tool_calls:
                # append assistant message with tool_calls
                msgs.append({
                    "role": "assistant",
                    "content": m.get("content"),
                    "tool_calls": tool_calls
                })
                for tc in tool_calls:
                    name  = tc["function"]["name"]
                    args  = tc["function"].get("arguments", "{}")
                    if isinstance(args, str):
                        try:
                            args = json.loads(args)
                        except Exception:
                            pass
                    called.append(name)
                    result = mock_results.get(name, {"error": "tool not available"})
                    print(f"  [TOOL]     {name}({json.dumps(args)}) -> {json.dumps(result)}")
                    # Groq requires tool_call_id in tool result messages
                    msgs.append({
                        "role": "tool",
                        "tool_call_id": tc["id"],
                        "content": json.dumps(result)
                    })
            else:
                text = m.get("content") or ""
                msgs.append({"role": "assistant", "content": text})
                print(f"  ASSISTANT: {text}")
                break

    final = next(
        (m.get("content", "") for m in reversed(msgs)
         if m.get("role") == "assistant" and m.get("content")),
        ""
    )
    return msgs, called, final


BOOKED_PHRASES = ["you're booked", "youre booked", "you are booked",
                  "all booked", "booking is confirmed", "successfully booked",
                  "appointment is confirmed", "appointment has been booked",
                  "all set", "is confirmed", "is booked", "have you booked",
                  "booking id", "booking reference"]


def has_booked_phrase(text):
    t = text.lower()
    return any(p in t for p in BOOKED_PHRASES)


SCENARIOS = [
    {
        "name": "S1 - Happy path: explicit yes, tool succeeds",
        "turns": [
            "I'd like to book a haircut next Friday after 3pm",
            "Yes please, go ahead and book it",
        ],
        "mock": {
            "check_availability": {"slot": "Friday 2026-11-27 15:30", "service": "haircut", "available": True},
            "book_appointment":   {"status": "success", "booking_id": "BK-001",
                                   "slot": "Friday 2026-11-27 15:30", "service": "haircut"},
        },
        "checks": {
            "check_availability called":   lambda c, f: "check_availability" in c,
            "book_appointment called":     lambda c, f: "book_appointment" in c,
            "says 'you're booked'":        lambda c, f: has_booked_phrase(f),
        },
    },
    {
        "name": "S2 - Ambiguous reply: not an explicit yes -> book_appointment NOT called",
        "turns": [
            "I'd like to book a haircut next Friday after 3pm",
            "What time did you say?",
        ],
        "mock": {
            "check_availability": {"slot": "Friday 2026-11-27 15:30", "service": "haircut", "available": True},
        },
        "checks": {
            "book_appointment NOT called":    lambda c, f: "book_appointment" not in c,
            "does NOT say 'you're booked'":   lambda c, f: not has_booked_phrase(f),
        },
    },
    {
        "name": "S3 - Tool failure: explicit yes, tool fails -> no 'you're booked'",
        "turns": [
            "Can I book a haircut for next Friday afternoon?",
            "Yes, go ahead",
        ],
        "mock": {
            "check_availability": {"slot": "Friday 2026-11-27 14:00", "service": "haircut", "available": True},
            "book_appointment":   {"status": "failed", "reason": "slot no longer available"},
        },
        "checks": {
            "book_appointment called":        lambda c, f: "book_appointment" in c,
            "does NOT say 'you're booked'":   lambda c, f: not has_booked_phrase(f),
        },
    },
]


def main():
    print(f"Prototype: booking confirmation gate (Groq hosted LLM)")
    print(f"Model:     {MODEL}")
    print(f"Date:      2026-11-21\n")

    all_results = []

    for s in SCENARIOS:
        print(f"\n{'='*66}")
        print(f"  {s['name']}")
        print(f"{'='*66}")
        msgs, called, final = run_scenario(s["turns"], s["mock"])
        checks = {}
        for label, fn in s["checks"].items():
            ok = fn(called, final)
            checks[label] = "PASS" if ok else "FAIL"
            marker = "+" if ok else "x"
            print(f"  [{marker}] [{checks[label]}] {label}")
        all_results.append({
            "scenario":   s["name"],
            "tool_calls": called,
            "final_text": final,
            "checks":     checks,
        })

    passed = sum(1 for r in all_results for v in r["checks"].values() if v == "PASS")
    total  = sum(len(r["checks"]) for r in all_results)
    verdict = "PASS - confirmation gate reliable" if passed == total \
              else f"FAIL - {total - passed} check(s) failed"

    print(f"\n{'='*66}")
    print(f"  RESULT: {passed}/{total} checks passed")
    print(f"  VERDICT: {verdict}")
    print(f"{'='*66}\n")

    record = {
        "model":   MODEL,
        "track":   "SaaS (Groq hosted)",
        "date":    "2026-11-21",
        "passed":  passed,
        "total":   total,
        "verdict": verdict,
        "results": all_results,
    }
    out = "prototype-results-groq.json"
    with open(out, "w") as f:
        json.dump(record, f, indent=2)
    print(f"Results written to {out}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
