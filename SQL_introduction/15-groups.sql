-- Select the score and the count of records with that score from second_table

SELECT score, COUNT (*) AS number
FROM second_table

-- Group by score

GROUP BY score

-- Order by number in descending order

ORDER BY number DESC;

