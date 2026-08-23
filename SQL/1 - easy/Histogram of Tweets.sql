SELECT count(*),user_id
FROM tweets
WHERE tweet_date >= '01/01/2022'
AND tweet_date <= '12/31/2022'
GROUP by user_id