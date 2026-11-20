-- Fictional scheduling data. SQLite compatible; no real patients or PHI.
DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS providers;
DROP TABLE IF EXISTS external_events;
CREATE TABLE providers (provider_id INTEGER PRIMARY KEY, display_name TEXT NOT NULL);
CREATE TABLE appointments (
  appointment_id INTEGER PRIMARY KEY,
  provider_id INTEGER,
  external_reference TEXT,
  appointment_status TEXT NOT NULL,
  start_at TEXT NOT NULL
);
CREATE TABLE external_events (
  external_reference TEXT NOT NULL,
  event_status TEXT NOT NULL
);
INSERT INTO providers VALUES (1, 'Provider A'), (2, 'Provider B');
INSERT INTO appointments VALUES
(101,1,'EXT-100','scheduled','2026-11-02T10:00:00'),
(102,2,'EXT-101','cancelled','2026-11-02T11:00:00'),
(103,999,'EXT-102','scheduled','2026-11-02T12:00:00'), -- orphaned provider
(104,1,'EXT-101','scheduled','2026-11-02T13:00:00'), -- duplicated external reference
(105,2,NULL,'scheduled','2026-11-03T10:00:00'); -- missing external reference
INSERT INTO external_events VALUES
('EXT-100','active'),('EXT-101','active'),('EXT-102','cancelled');
