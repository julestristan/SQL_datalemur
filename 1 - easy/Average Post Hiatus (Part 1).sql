SELECT
  user_id,
  MAX(post_date::DATE) - MIN(post_date::DATE) as days_diff
FROM posts
WHERE
	DATE_PART('year',post_date::date)=2021 
GROUP BY user_id
HAVING count(post_id) > 1