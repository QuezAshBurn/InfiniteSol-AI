#!/usr/bin/env python3
"""
ponytail: booking confirmation gate prototype
Question: does llama3.1:8b follow the two-part gate rule?
  (1) only call book_appointment after explicit customer confirmation
  (2) only say 'you're booked' after tool returns {"status": "success"}
Evidence: 3 synthetic booking conversations with mock tools
"""
import io, json, sys, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

OLLAMA = "http://localhost:11434/api/chat"
MODEL  = "llama3.1:8b"

SYSTEM = """\
You are a voice assistant for appointment scheduling. Be hospitable, respectful, and jolly.
Stay calm and helpful if a customer is frustrated or a booking fails.

BOOKING RULES — follow exactly:
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


def call_ollama(messages):
    body = json.dumps({
        "model": MODEL, "messages": messages, "tools": TOOLS, "stream": False
    }).encode()
    req = urllib.request.Request(
        OLLAMA, data=body, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.loads(r.read())["message"]


def run_scenario(turns, mock_results):
    """
    turns        – list of user utterance strings
    mock_results – dict of tool_name -> result dict

    Returns (all_messages, list_of_tool_names_called, final_assistant_text)
    """
    msgs   = [{"role": "system", "content": SYSTEM}]
    called = []

    for user_text in turns:
        msgs.append({"role": "user", "content": user_text})
        print(f"  USER:      {user_text}")

        # Let the model respond, handling any tool call loop
        while True:
            m = call_ollama(msgs)
            msgs.append(m)

            if m.get("tool_calls"):
                for tc in m["tool_calls"]:
                    name = tc["function"]["name"]
                    args = tc["function"].get("arguments", {})
                    if isinstance(args, str):          # some Ollama builds stringify args
                        try:
                            args = json.loads(args)
                        except Exception:
                            pass
                    called.append(name)
                    result = mock_results.get(name, {"error": "tool not available"})
                    print(f"  [TOOL]     {name}({json.dumps(args)}) -> {json.dumps(result)}")
                    msgs.append({
                        "role": "tool", "name": name, "content": json.dumps(result)
                    })
                # loop: model may now produce a text response or another tool call
            else:
                text = m.get("content") or ""
                print(f"  ASSISTANT: {text}")
                break  # text response — advance to next user turn

    final = next(
        (m.get("content", "") for m in reversed(msgs)
         if m.get("role") == "assistant" and m.get("content")),
        ""
    )
    return msgs, called, final


BOOKED_PHRASES = ["you're booked", "youre booked", "you are booked",
                  "all booked", "booking is confirmed", "successfully booked",
                  "appointment is confirmed", "appointment has been booked"]


def has_booked_phrase(text):
    t = text.lower()
    return any(p in t for p in BOOKED_PHRASES)


SCENARIOS = [
    {
        "name": "S1 - Happy path: explicit yes, tool succeeds -> 'you're booked'",
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
            "What time did you say?",           # ambiguous — not a yes
        ],
        "mock": {
            "check_availability": {"slot": "Friday 2026-11-27 15:30", "service": "haircut", "available": True},
            # book_appointment intentionally absent — should not be reached
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
    print(f"Prototype: booking confirmation gate")
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
            marker = "✓" if ok else "✗"
            print(f"  [{checks[label]}] {label}")
        all_results.append({
            "scenario":   s["name"],
            "tool_calls": called,
            "final_text": final,
            "checks":     checks,
        })

    passed = sum(1 for r in all_results for v in r["checks"].values() if v == "PASS")
    total  = sum(len(r["checks"]) for r in all_results)
    verdict = "PASS — confirmation gate reliable" if passed == total else f"FAIL — {total - passed} check(s) failed"

    print(f"\n{'='*66}")
    print(f"  RESULT: {passed}/{total} checks passed")
    print(f"  VERDICT: {verdict}")
    print(f"{'='*66}\n")

    record = {
        "model":   MODEL,
        "date":    "2026-11-21",
        "passed":  passed,
        "total":   total,
        "verdict": verdict,
        "results": all_results,
    }
    with open("prototype-results.json", "w") as f:
        json.dump(record, f, indent=2)
    print("Results written to prototype-results.json")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
