-- Select the score and the name columns from second_table

SELECT score, name
FROM second_table

-- Filter out rows without a name value

WHERE name IS NOT NULL

-- Order by score in descending order

ORDER BY score DESC;

