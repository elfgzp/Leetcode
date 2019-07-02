SELECT
  a.score AS Score,
  COUNT(DISTINCT b.score) AS Rank
FROM
  scores a LEFT JOIN scores b ON
  a.score <= b.score
GROUP BY a.id
ORDER BY a.score DESC

