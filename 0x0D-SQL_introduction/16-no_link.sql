-- List all records from the 'second table' without using any links.
SELECT score, name
FROM second_table;
WHERE 'name IS NOT NULL';
ORDER BY score DESC;