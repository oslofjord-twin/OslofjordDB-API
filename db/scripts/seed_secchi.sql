-- Seed 5 Secchi disk measurements placed at the centroid of an existing grid cell,
-- so every reading lands inside the fjord's surveyed area. Re-running is safe.

DELETE FROM secchi_depth WHERE source = 'seed-demo';

WITH picks AS (
    SELECT id, geom, row_number() OVER (ORDER BY id) AS rn
    FROM grid
    WHERE id IN (170, 211, 254, 298)
),
demo(rn, hours_ago, depth_m, quality, note) AS (
    VALUES
        (1, 48, 5.8::numeric, 0.93::numeric, 'Outer fjord, very clear'),
        (2, 26,  2.4::numeric, 0.78::numeric, 'Post-rain runoff'),
        (3, 14,  4.7::numeric, 0.91::numeric, 'Clear, classified by secchi-sort'),
        (4,  1,  1.8::numeric, 0.72::numeric, 'Algae bloom suspected')
)
INSERT INTO secchi_depth (record_time, depth_m, location, grid_id, source, quality, note)
SELECT
    NOW() - (d.hours_ago || ' hours')::interval,
    d.depth_m,
    ST_Centroid(p.geom)::geography,
    p.id,
    'seed-demo',
    d.quality,
    d.note
FROM picks p
JOIN demo d ON p.rn = d.rn;
