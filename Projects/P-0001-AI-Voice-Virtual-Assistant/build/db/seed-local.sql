-- Local dev seed — P-0001 synthetic tenants T1 and T2
-- Run: wrangler d1 execute p0001-va-db --local --file=build/db/seed-local.sql

-- ── T1: Riverside Hair Studio (Aria) ────────────────────────────────────────
INSERT OR REPLACE INTO tenants VALUES (
  't1', 'Riverside Hair Studio', 'Aria', '61400000001', 'en'
);

INSERT OR REPLACE INTO tool_approvals VALUES ('t1', 'check_availability', 1);
INSERT OR REPLACE INTO tool_approvals VALUES ('t1', 'book_appointment', 1);

INSERT OR REPLACE INTO services VALUES ('t1-haircut',    't1', 'Haircut',         45, 65.0);
INSERT OR REPLACE INTO services VALUES ('t1-colour',     't1', 'Colour Treatment', 90, 150.0);
INSERT OR REPLACE INTO services VALUES ('t1-blowdry',    't1', 'Blow Dry',         30, 45.0);

INSERT OR REPLACE INTO time_slots VALUES ('t1-s1', 't1', 't1-haircut',  '2026-11-24 09:00', '2026-11-24 09:45', 1);
INSERT OR REPLACE INTO time_slots VALUES ('t1-s2', 't1', 't1-haircut',  '2026-11-24 10:00', '2026-11-24 10:45', 1);
INSERT OR REPLACE INTO time_slots VALUES ('t1-s3', 't1', 't1-colour',   '2026-11-24 11:00', '2026-11-24 12:30', 1);
INSERT OR REPLACE INTO time_slots VALUES ('t1-s4', 't1', 't1-blowdry',  '2026-11-24 13:00', '2026-11-24 13:30', 1);
INSERT OR REPLACE INTO time_slots VALUES ('t1-s5', 't1', 't1-haircut',  '2026-11-25 09:00', '2026-11-25 09:45', 1);

INSERT OR REPLACE INTO knowledge_sources VALUES (
  'faq', 't1',
  'Riverside Hair Studio — FAQ',
  'We are located at 12 River St, Riverside. Open Mon–Sat 9am–6pm. Free parking on site. We accept card and cash. Products used: Kerastase and Olaplex. Walk-ins welcome subject to availability.',
  '1.0', datetime('now')
);

-- ── T2: Peak Physio Clinic (Max) ────────────────────────────────────────────
INSERT OR REPLACE INTO tenants VALUES (
  't2', 'Peak Physio Clinic', 'Max', '61400000002', 'en'
);

INSERT OR REPLACE INTO tool_approvals VALUES ('t2', 'check_availability', 1);
INSERT OR REPLACE INTO tool_approvals VALUES ('t2', 'book_appointment', 1);

INSERT OR REPLACE INTO services VALUES ('t2-initial',  't2', 'Initial Assessment', 60, 120.0);
INSERT OR REPLACE INTO services VALUES ('t2-followup', 't2', 'Follow-up Session',  30, 80.0);
INSERT OR REPLACE INTO services VALUES ('t2-massage',  't2', 'Sports Massage',     45, 95.0);

INSERT OR REPLACE INTO time_slots VALUES ('t2-s1', 't2', 't2-initial',  '2026-11-24 08:00', '2026-11-24 09:00', 1);
INSERT OR REPLACE INTO time_slots VALUES ('t2-s2', 't2', 't2-followup', '2026-11-24 09:00', '2026-11-24 09:30', 1);
INSERT OR REPLACE INTO time_slots VALUES ('t2-s3', 't2', 't2-massage',  '2026-11-24 10:00', '2026-11-24 10:45', 1);
INSERT OR REPLACE INTO time_slots VALUES ('t2-s4', 't2', 't2-initial',  '2026-11-25 08:00', '2026-11-25 09:00', 1);

INSERT OR REPLACE INTO knowledge_sources VALUES (
  'faq', 't2',
  'Peak Physio Clinic — FAQ',
  'Located at 88 Summit Rd, Northside. Open Mon–Fri 8am–7pm, Sat 9am–2pm. Medicare rebates available with GP referral. HICAPS on-site for private health claims. Specialties: sports injury, post-surgical rehab, dry needling.',
  '1.0', datetime('now')
);
