-- 1. INNER JOIN:
-- Pair every meter reading with its meter.

SELECT
    m.meter_id,
    m.meter_number,
    m.location,
    r.reading_id,
    r.reading_value,
    r.reading_date
FROM meters AS m
INNER JOIN readings AS r
    ON m.meter_id = r.meter_id
ORDER BY m.meter_id, r.reading_date;


-- 2. LEFT JOIN:
-- Find meters that have no readings.

SELECT
    m.meter_id,
    m.meter_number,
    m.location
FROM meters AS m
LEFT JOIN readings AS r
    ON m.meter_id = r.meter_id
WHERE r.reading_id IS NULL
ORDER BY m.meter_id;
