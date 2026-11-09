-- cases.newarkfirm.com — D1 initial schema
-- Each desk has its own queue table to allow independent pagination/indexing.

CREATE TABLE IF NOT EXISTS queue_patent (
  id TEXT PRIMARY KEY,
  docket_id INTEGER NOT NULL,
  case_number TEXT NOT NULL,
  case_name TEXT NOT NULL,
  court TEXT NOT NULL,
  nos_code INTEGER NOT NULL,
  date_filed TEXT NOT NULL,
  date_ingested TEXT NOT NULL DEFAULT (datetime('now')),
  plaintiff_counsel TEXT,
  defendant_counsel TEXT,
  status TEXT NOT NULL DEFAULT 'new',
  source_alert_id INTEGER,
  raw_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS queue_ada (
  id TEXT PRIMARY KEY,
  docket_id INTEGER NOT NULL,
  case_number TEXT NOT NULL,
  case_name TEXT NOT NULL,
  court TEXT NOT NULL,
  nos_code INTEGER NOT NULL,
  date_filed TEXT NOT NULL,
  date_ingested TEXT NOT NULL DEFAULT (datetime('now')),
  plaintiff_counsel TEXT,
  defendant_counsel TEXT,
  status TEXT NOT NULL DEFAULT 'new',
  source_alert_id INTEGER,
  raw_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS queue_workplace (
  id TEXT PRIMARY KEY,
  docket_id INTEGER NOT NULL,
  case_number TEXT NOT NULL,
  case_name TEXT NOT NULL,
  court TEXT NOT NULL,
  nos_code INTEGER NOT NULL,
  date_filed TEXT NOT NULL,
  date_ingested TEXT NOT NULL DEFAULT (datetime('now')),
  plaintiff_counsel TEXT,
  defendant_counsel TEXT,
  status TEXT NOT NULL DEFAULT 'new',
  source_alert_id INTEGER,
  raw_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS queue_insurance (
  id TEXT PRIMARY KEY,
  docket_id INTEGER NOT NULL,
  case_number TEXT NOT NULL,
  case_name TEXT NOT NULL,
  court TEXT NOT NULL,
  nos_code INTEGER NOT NULL,
  date_filed TEXT NOT NULL,
  date_ingested TEXT NOT NULL DEFAULT (datetime('now')),
  plaintiff_counsel TEXT,
  defendant_counsel TEXT,
  status TEXT NOT NULL DEFAULT 'new',
  source_alert_id INTEGER,
  raw_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS queue_trucking (
  id TEXT PRIMARY KEY,
  docket_id INTEGER NOT NULL,
  case_number TEXT NOT NULL,
  case_name TEXT NOT NULL,
  court TEXT NOT NULL,
  nos_code INTEGER NOT NULL,
  date_filed TEXT NOT NULL,
  date_ingested TEXT NOT NULL DEFAULT (datetime('now')),
  plaintiff_counsel TEXT,
  defendant_counsel TEXT,
  status TEXT NOT NULL DEFAULT 'new',
  source_alert_id INTEGER,
  raw_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS queue_aviation (
  id TEXT PRIMARY KEY,
  docket_id INTEGER NOT NULL,
  case_number TEXT NOT NULL,
  case_name TEXT NOT NULL,
  court TEXT NOT NULL,
  nos_code INTEGER NOT NULL,
  date_filed TEXT NOT NULL,
  date_ingested TEXT NOT NULL DEFAULT (datetime('now')),
  plaintiff_counsel TEXT,
  defendant_counsel TEXT,
  status TEXT NOT NULL DEFAULT 'new',
  source_alert_id INTEGER,
  raw_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS queue_maritime (
  id TEXT PRIMARY KEY,
  docket_id INTEGER NOT NULL,
  case_number TEXT NOT NULL,
  case_name TEXT NOT NULL,
  court TEXT NOT NULL,
  nos_code INTEGER NOT NULL,
  date_filed TEXT NOT NULL,
  date_ingested TEXT NOT NULL DEFAULT (datetime('now')),
  plaintiff_counsel TEXT,
  defendant_counsel TEXT,
  status TEXT NOT NULL DEFAULT 'new',
  source_alert_id INTEGER,
  raw_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS queue_pi (
  id TEXT PRIMARY KEY,
  docket_id INTEGER NOT NULL,
  case_number TEXT NOT NULL,
  case_name TEXT NOT NULL,
  court TEXT NOT NULL,
  nos_code INTEGER NOT NULL,
  date_filed TEXT NOT NULL,
  date_ingested TEXT NOT NULL DEFAULT (datetime('now')),
  plaintiff_counsel TEXT,
  defendant_counsel TEXT,
  status TEXT NOT NULL DEFAULT 'new',
  source_alert_id INTEGER,
  raw_json TEXT NOT NULL
);

-- Per-desk metadata: last ingest timestamp, alert registration status, overview count cache
CREATE TABLE IF NOT EXISTS desk_meta (
  desk_id TEXT PRIMARY KEY,
  last_ingest_at TEXT,
  alert_id INTEGER,
  alert_status TEXT DEFAULT 'unknown',
  overview_count INTEGER DEFAULT 0,
  updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Seed desk_meta rows
INSERT OR IGNORE INTO desk_meta (desk_id) VALUES
  ('patent'), ('ada'), ('workplace'), ('insurance'),
  ('trucking'), ('aviation'), ('maritime'), ('pi');

-- Indexes for common queries
CREATE INDEX IF NOT EXISTS idx_patent_date   ON queue_patent(date_filed DESC);
CREATE INDEX IF NOT EXISTS idx_ada_date      ON queue_ada(date_filed DESC);
CREATE INDEX IF NOT EXISTS idx_workplace_date ON queue_workplace(date_filed DESC);
CREATE INDEX IF NOT EXISTS idx_insurance_date ON queue_insurance(date_filed DESC);
CREATE INDEX IF NOT EXISTS idx_trucking_date ON queue_trucking(date_filed DESC);
CREATE INDEX IF NOT EXISTS idx_aviation_date ON queue_aviation(date_filed DESC);
CREATE INDEX IF NOT EXISTS idx_maritime_date ON queue_maritime(date_filed DESC);
CREATE INDEX IF NOT EXISTS idx_pi_date       ON queue_pi(date_filed DESC);
