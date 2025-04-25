WITH matched AS (
  SELECT f.id, s.status
  FROM full_names f
  JOIN short_names s ON s.name = split_part(f.name, '.', 1)
)
UPDATE full_names f
SET status = matched.status
FROM matched
WHERE f.id = matched.id;
