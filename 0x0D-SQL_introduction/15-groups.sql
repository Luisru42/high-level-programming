-- List the number of records with the same score in the 'second table'.
SELECT score, COUNT('score') AS number
FROM `second table`
GROUP BY score;
ORDER BY number DESC;
-- --- IGNORE ---