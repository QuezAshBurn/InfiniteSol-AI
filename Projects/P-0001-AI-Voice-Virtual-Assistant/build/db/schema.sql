-- P-0001 AI Voice Virtual Assistant — D1 schema
-- Cloudflare D1 (SQLite-compatible)

CREATE TABLE IF NOT EXISTS tenants (
  tenant_id        TEXT PRIMARY KEY,
  name             TEXT NOT NULL,
  va_name          TEXT NOT NULL,
  whatsapp_number  TEXT UNIQUE NOT NULL,  -- the number customers message
  language_default TEXT NOT NULL DEFAULT 'en'
);

-- SEC-003: approval checked per-call, not cached
CREATE TABLE IF NOT EXISTS tool_approvals (
  tenant_id  TEXT NOT NULL,
  tool_name  TEXT NOT NULL,
  approved   INTEGER NOT NULL DEFAULT 1,
  PRIMARY KEY (tenant_id, tool_name),
  FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id)
);

CREATE TABLE IF NOT EXISTS services (
  service_id       TEXT NOT NULL,
  tenant_id        TEXT NOT NULL,
  name             TEXT NOT NULL,
  duration_minutes INTEGER NOT NULL,
  price_aud        REAL,
  PRIMARY KEY (service_id, tenant_id),
  FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id)
);

CREATE TABLE IF NOT EXISTS time_slots (
  slot_id        TEXT PRIMARY KEY,
  tenant_id      TEXT NOT NULL,
  service_id     TEXT NOT NULL,
  start_datetime TEXT NOT NULL,  -- ISO 8601, local time
  end_datetime   TEXT NOT NULL,
  available      INTEGER NOT NULL DEFAULT 1,
  FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id)
);

-- bookings: one row per confirmed booking
CREATE TABLE IF NOT EXISTS bookings (
  booking_id       TEXT PRIMARY KEY,
  tenant_id        TEXT NOT NULL,
  service_id       TEXT NOT NULL,
  slot_id          TEXT NOT NULL UNIQUE,
  customer_phone   TEXT NOT NULL,
  customer_email   TEXT,
  idempotency_key  TEXT UNIQUE NOT NULL,  -- prevents duplicate writes
  created_at       TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id)
);

-- human handoff requests
CREATE TABLE IF NOT EXISTS handoff_requests (
  request_id      TEXT PRIMARY KEY,
  tenant_id       TEXT NOT NULL,
  customer_phone  TEXT NOT NULL,
  customer_email  TEXT,
  reason          TEXT,
  created_at      TEXT NOT NULL DEFAULT (datetime('now')),
  resolved        INTEGER NOT NULL DEFAULT 0,
  FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id)
);

-- knowledge sources for RAG (phase 1: full text; phase 2: Vectorize embeddings)
CREATE TABLE IF NOT EXISTS knowledge_sources (
  source_id   TEXT NOT NULL,
  tenant_id   TEXT NOT NULL,
  title       TEXT NOT NULL,
  content     TEXT NOT NULL,
  revision    TEXT NOT NULL DEFAULT '1.0',
  updated_at  TEXT NOT NULL DEFAULT (datetime('now')),
  PRIMARY KEY (source_id, tenant_id),
  FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id)
);

CREATE INDEX IF NOT EXISTS idx_time_slots_tenant_available
  ON time_slots (tenant_id, available, start_datetime);

CREATE INDEX IF NOT EXISTS idx_bookings_tenant
  ON bookings (tenant_id, customer_phone);
