// D1-backed tool implementations

// SEC-003: check tool approval before each call (not cached)
async function checkToolApproval(tenantId, toolName, db) {
  const row = await db.prepare(
    'SELECT approved FROM tool_approvals WHERE tenant_id = ? AND tool_name = ?'
  ).bind(tenantId, toolName).first();
  return row?.approved === 1;
}

// Returns up to 5 available slots for a service, ordered by start_datetime
export async function checkAvailability(args, tenantId, db) {
  const { service_name, preferred_date } = args;

  // SEC-003
  if (!await checkToolApproval(tenantId, 'check_availability', db)) {
    return { error: 'Tool not approved for this tenant.' };
  }

  let query, bindings;
  if (preferred_date) {
    query = `
      SELECT ts.slot_id, s.name AS service_name, ts.start_datetime, ts.end_datetime
      FROM time_slots ts
      JOIN services s ON ts.service_id = s.service_id AND ts.tenant_id = s.tenant_id
      WHERE ts.tenant_id = ?
        AND s.name = ?
        AND ts.available = 1
        AND date(ts.start_datetime) = ?
      ORDER BY ts.start_datetime
      LIMIT 5
    `;
    bindings = [tenantId, service_name, preferred_date];
  } else {
    query = `
      SELECT ts.slot_id, s.name AS service_name, ts.start_datetime, ts.end_datetime
      FROM time_slots ts
      JOIN services s ON ts.service_id = s.service_id AND ts.tenant_id = s.tenant_id
      WHERE ts.tenant_id = ?
        AND s.name = ?
        AND ts.available = 1
      ORDER BY ts.start_datetime
      LIMIT 5
    `;
    bindings = [tenantId, service_name];
  }

  const { results } = await db.prepare(query).bind(...bindings).all();

  if (!results.length) {
    return { slots: [], message: 'No available slots found for that service and date.' };
  }

  return {
    slots: results.map(r => ({
      slot_id: r.slot_id,
      service_name: r.service_name,
      start: r.start_datetime,
      end: r.end_datetime,
    })),
  };
}

// Books a slot. Returns { status: 'success', booking_id } or { status: 'error', reason }.
export async function bookAppointment(args, tenantId, customerPhone, db) {
  const { slot_id, service_name } = args;

  // SEC-003
  if (!await checkToolApproval(tenantId, 'book_appointment', db)) {
    return { status: 'error', reason: 'Tool not approved for this tenant.' };
  }

  // SEC-002: verify slot belongs to this tenant
  const slot = await db.prepare(
    'SELECT slot_id, tenant_id, service_id, available, start_datetime, end_datetime FROM time_slots WHERE slot_id = ? AND tenant_id = ?'
  ).bind(slot_id, tenantId).first();

  if (!slot) {
    return { status: 'error', reason: 'Slot not found or does not belong to this business.' };
  }
  if (!slot.available) {
    return { status: 'error', reason: 'That slot is no longer available.' };
  }

  const bookingId = crypto.randomUUID();
  // ponytail: idempotency key = tenantId + slotId; prevents duplicate bookings on retry
  const idempotencyKey = `${tenantId}:${slot_id}`;

  try {
    await db.batch([
      db.prepare(
        `INSERT INTO bookings (booking_id, tenant_id, service_id, slot_id, customer_phone, idempotency_key)
         VALUES (?, ?, ?, ?, ?, ?)`
      ).bind(bookingId, tenantId, slot.service_id, slot_id, customerPhone, idempotencyKey),
      db.prepare(
        'UPDATE time_slots SET available = 0 WHERE slot_id = ? AND tenant_id = ?'
      ).bind(slot_id, tenantId),
    ]);
  } catch (err) {
    // UNIQUE constraint on idempotency_key = already booked
    if (err.message?.includes('UNIQUE') || err.message?.includes('unique')) {
      return { status: 'error', reason: 'That slot was just booked. Please choose another time.' };
    }
    throw err;
  }

  // "2026-11-24 09:00" → "20261124T090000" for Google Calendar URL
  function toGcalDate(dt) {
    const s = dt.replace(/[-: ]/g, '');
    return `${s.slice(0, 8)}T${s.slice(8)}00`;
  }
  const calendar_url = `https://calendar.google.com/calendar/render?action=TEMPLATE` +
    `&text=${encodeURIComponent(service_name)}` +
    `&dates=${toGcalDate(slot.start_datetime)}/${toGcalDate(slot.end_datetime)}`;

  return { status: 'success', booking_id: bookingId, service_name, slot_id, calendar_url };
}

// Records a human handoff request in D1
export async function recordHandoff(tenantId, customerPhone, customerEmail, reason, db) {
  const requestId = crypto.randomUUID();
  await db.prepare(
    `INSERT INTO handoff_requests (request_id, tenant_id, customer_phone, customer_email, reason)
     VALUES (?, ?, ?, ?, ?)`
  ).bind(requestId, tenantId, customerPhone, customerEmail || null, reason || null).run();
  return requestId;
}
