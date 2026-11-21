-- Seed data: T1 — Riverside Hair Studio
-- Replace whatsapp_number with the actual Meta-approved number at deploy

INSERT OR REPLACE INTO tenants VALUES
  ('T1', 'Riverside Hair Studio', 'Aria', '+61400000001', 'en');

INSERT OR REPLACE INTO tool_approvals VALUES
  ('T1', 'check_availability', 1),
  ('T1', 'book_appointment', 1);

INSERT OR REPLACE INTO services VALUES
  ('T1-SVC001', 'T1', 'Haircut',  30, 35.00),
  ('T1-SVC002', 'T1', 'Colour',  120, 120.00),
  ('T1-SVC003', 'T1', 'Blowout',  45, 55.00);

-- Slots: week of 24 Nov 2026 (Mon–Sat)
-- Haircut slots (30 min)
INSERT OR REPLACE INTO time_slots VALUES
  ('T1-SL001', 'T1', 'T1-SVC001', '2026-11-24 09:00', '2026-11-24 09:30', 1),
  ('T1-SL002', 'T1', 'T1-SVC001', '2026-11-24 14:00', '2026-11-24 14:30', 1),
  ('T1-SL003', 'T1', 'T1-SVC001', '2026-11-25 10:00', '2026-11-25 10:30', 1),
  ('T1-SL004', 'T1', 'T1-SVC001', '2026-11-25 15:00', '2026-11-25 15:30', 1),
  ('T1-SL005', 'T1', 'T1-SVC001', '2026-11-26 09:00', '2026-11-26 09:30', 1),
  ('T1-SL006', 'T1', 'T1-SVC001', '2026-11-27 11:00', '2026-11-27 11:30', 1),
  ('T1-SL007', 'T1', 'T1-SVC001', '2026-11-27 14:00', '2026-11-27 14:30', 1),
  ('T1-SL008', 'T1', 'T1-SVC001', '2026-11-28 09:00', '2026-11-28 09:30', 1),
  ('T1-SL009', 'T1', 'T1-SVC001', '2026-11-28 15:00', '2026-11-28 15:30', 1);

-- Colour slots (120 min)
INSERT OR REPLACE INTO time_slots VALUES
  ('T1-SL010', 'T1', 'T1-SVC002', '2026-11-24 09:00', '2026-11-24 11:00', 1),
  ('T1-SL011', 'T1', 'T1-SVC002', '2026-11-25 14:00', '2026-11-25 16:00', 1),
  ('T1-SL012', 'T1', 'T1-SVC002', '2026-11-26 09:00', '2026-11-26 11:00', 1),
  ('T1-SL013', 'T1', 'T1-SVC002', '2026-11-27 09:00', '2026-11-27 11:00', 1),
  ('T1-SL014', 'T1', 'T1-SVC002', '2026-11-28 14:00', '2026-11-28 16:00', 1);

-- Blowout slots (45 min)
INSERT OR REPLACE INTO time_slots VALUES
  ('T1-SL015', 'T1', 'T1-SVC003', '2026-11-24 10:00', '2026-11-24 10:45', 1),
  ('T1-SL016', 'T1', 'T1-SVC003', '2026-11-24 15:00', '2026-11-24 15:45', 1),
  ('T1-SL017', 'T1', 'T1-SVC003', '2026-11-25 09:00', '2026-11-25 09:45', 1),
  ('T1-SL018', 'T1', 'T1-SVC003', '2026-11-26 14:00', '2026-11-26 14:45', 1),
  ('T1-SL019', 'T1', 'T1-SVC003', '2026-11-27 10:00', '2026-11-27 10:45', 1),
  ('T1-SL020', 'T1', 'T1-SVC003', '2026-11-28 11:00', '2026-11-28 11:45', 1);

INSERT OR REPLACE INTO knowledge_sources VALUES
  ('T1-KB001', 'T1', 'Services and Pricing',
   'Riverside Hair Studio offers the following services:
- Haircut: 30 minutes, AUD 35. Includes wash, cut, and blow-dry.
- Colour: 2 hours, AUD 120. Full colour treatment including toner and conditioning.
- Blowout: 45 minutes, AUD 55. Professional blow-dry and styling.

All services include a complimentary scalp massage.',
   '1.0', datetime('now')),

  ('T1-KB002', 'T1', 'Operating Hours and Location',
   'Riverside Hair Studio is open Tuesday to Saturday, 9 AM to 6 PM. We are closed on Sundays and Mondays.
Location: 12 Riverside Drive, Melbourne VIC 3000.
Phone: (03) 9000 1234.
We are located near the Riverside tram stop, with 2-hour street parking available.',
   '1.0', datetime('now')),

  ('T1-KB003', 'T1', 'Booking and Cancellation Policy',
   'Bookings can be made via our WhatsApp voice assistant. We require 24 hours notice for cancellations.
Late cancellations (less than 24 hours) may incur a 50% cancellation fee.
Walk-ins are welcome subject to availability.
Gift vouchers are available — ask our team for details.',
   '1.0', datetime('now'));
