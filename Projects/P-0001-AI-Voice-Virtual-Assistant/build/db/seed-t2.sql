-- Seed data: T2 — Peak Physio Clinic
-- Replace whatsapp_number with the actual Meta-approved number at deploy

INSERT OR REPLACE INTO tenants VALUES
  ('T2', 'Peak Physio Clinic', 'Max', '+61400000002', 'en');

INSERT OR REPLACE INTO tool_approvals VALUES
  ('T2', 'check_availability', 1),
  ('T2', 'book_appointment', 1);

INSERT OR REPLACE INTO services VALUES
  ('T2-SVC001', 'T2', 'Initial Assessment', 60, 90.00),
  ('T2-SVC002', 'T2', 'Follow-up',          30, 60.00),
  ('T2-SVC003', 'T2', 'Sports Rehab',       45, 75.00);

-- Slots: week of 24 Nov 2026 (Mon–Fri, clinic is closed Sat/Sun)
-- Initial Assessment slots (60 min)
INSERT OR REPLACE INTO time_slots VALUES
  ('T2-SL001', 'T2', 'T2-SVC001', '2026-11-24 09:00', '2026-11-24 10:00', 1),
  ('T2-SL002', 'T2', 'T2-SVC001', '2026-11-24 14:00', '2026-11-24 15:00', 1),
  ('T2-SL003', 'T2', 'T2-SVC001', '2026-11-25 09:00', '2026-11-25 10:00', 1),
  ('T2-SL004', 'T2', 'T2-SVC001', '2026-11-26 14:00', '2026-11-26 15:00', 1),
  ('T2-SL005', 'T2', 'T2-SVC001', '2026-11-27 09:00', '2026-11-27 10:00', 1),
  ('T2-SL006', 'T2', 'T2-SVC001', '2026-11-28 14:00', '2026-11-28 15:00', 1);

-- Follow-up slots (30 min)
INSERT OR REPLACE INTO time_slots VALUES
  ('T2-SL007', 'T2', 'T2-SVC002', '2026-11-24 10:00', '2026-11-24 10:30', 1),
  ('T2-SL008', 'T2', 'T2-SVC002', '2026-11-24 15:00', '2026-11-24 15:30', 1),
  ('T2-SL009', 'T2', 'T2-SVC002', '2026-11-25 10:00', '2026-11-25 10:30', 1),
  ('T2-SL010', 'T2', 'T2-SVC002', '2026-11-25 15:00', '2026-11-25 15:30', 1),
  ('T2-SL011', 'T2', 'T2-SVC002', '2026-11-26 09:00', '2026-11-26 09:30', 1),
  ('T2-SL012', 'T2', 'T2-SVC002', '2026-11-27 11:00', '2026-11-27 11:30', 1),
  ('T2-SL013', 'T2', 'T2-SVC002', '2026-11-28 10:00', '2026-11-28 10:30', 1),
  ('T2-SL014', 'T2', 'T2-SVC002', '2026-11-28 15:00', '2026-11-28 15:30', 1);

-- Sports Rehab slots (45 min)
INSERT OR REPLACE INTO time_slots VALUES
  ('T2-SL015', 'T2', 'T2-SVC003', '2026-11-24 11:00', '2026-11-24 11:45', 1),
  ('T2-SL016', 'T2', 'T2-SVC003', '2026-11-25 14:00', '2026-11-25 14:45', 1),
  ('T2-SL017', 'T2', 'T2-SVC003', '2026-11-26 10:00', '2026-11-26 10:45', 1),
  ('T2-SL018', 'T2', 'T2-SVC003', '2026-11-27 14:00', '2026-11-27 14:45', 1),
  ('T2-SL019', 'T2', 'T2-SVC003', '2026-11-28 11:00', '2026-11-28 11:45', 1);

INSERT OR REPLACE INTO knowledge_sources VALUES
  ('T2-KB001', 'T2', 'Services and Pricing',
   'Peak Physio Clinic offers the following services:
- Initial Assessment: 60 minutes, AUD 90. Comprehensive musculoskeletal examination and treatment plan.
- Follow-up: 30 minutes, AUD 60. Progress review and ongoing treatment.
- Sports Rehab: 45 minutes, AUD 75. Sport-specific rehabilitation and injury prevention.

All services are eligible for private health insurance rebates. Medicare bulk-billing is available with a valid GP referral for Enhanced Primary Care (EPC) plans.',
   '1.0', datetime('now')),

  ('T2-KB002', 'T2', 'Operating Hours and Location',
   'Peak Physio Clinic is open Monday to Friday, 8 AM to 6 PM, and Saturday 8 AM to 12 PM. We are closed on Sundays.
Location: 45 Peak Street, Melbourne VIC 3001.
Phone: (03) 9000 5678.
Free parking is available in the building basement. We are a 5-minute walk from Flinders Street Station.',
   '1.0', datetime('now')),

  ('T2-KB003', 'T2', 'Referral and Cancellation Policy',
   'A GP referral is not required for most services, but is needed for Medicare EPC bulk-billing.
Please bring any relevant scans or imaging to your first appointment.
We require 24 hours notice for cancellations. Late cancellations may incur a fee.
Telehealth appointments are available for follow-ups — ask our team when booking.',
   '1.0', datetime('now'));
