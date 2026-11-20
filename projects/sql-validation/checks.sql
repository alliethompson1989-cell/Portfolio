-- Check 1: appointments referencing non-existent providers.
SELECT a.appointment_id, a.provider_id
FROM appointments AS a
LEFT JOIN providers AS p ON a.provider_id = p.provider_id
WHERE p.provider_id IS NULL;

-- Check 2: external references appearing more than once.
SELECT external_reference, COUNT(*) AS records
FROM appointments
WHERE external_reference IS NOT NULL
GROUP BY external_reference
HAVING COUNT(*) > 1;

-- Check 3: status inconsistent with the corresponding external event.
-- Assumes active = scheduled, cancelled = cancelled, just for this demo.
SELECT a.appointment_id, a.appointment_status, e.event_status
FROM appointments AS a
JOIN external_events AS e ON a.external_reference = e.external_reference
WHERE (a.appointment_status = 'scheduled' AND e.event_status <> 'active')
   OR (a.appointment_status = 'cancelled' AND e.event_status <> 'cancelled');

-- Check 4: missing external references.
SELECT appointment_id
FROM appointments
WHERE external_reference IS NULL OR TRIM(external_reference) = '';
