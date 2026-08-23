#1
SELECT distinct candidate_id 
FROM candidates
WHERE candidate_id IN (SELECT candidate_id FROM candidates WHERE skill = 'Python') 
  AND candidate_id IN (SELECT candidate_id FROM candidates WHERE skill = 'PostgreSQL') 
  AND candidate_id IN (SELECT candidate_id FROM candidates WHERE skill = 'Tableau') 
ORDER BY candidate_id ASC;



#2
SELECT candidate_id 
FROM candidates
WHERE skill IN ('Python', 'PostgreSQL', 'Tableau')
GROUP BY candidate_id
HAVING COUNT(DISTINCT skill) = 3
ORDER BY candidate_id ASC;