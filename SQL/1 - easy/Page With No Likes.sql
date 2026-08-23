SELECT
  pages.page_id
FROM pages
LEFT JOIN page_likes on pages.page_id = page_likes.page_id
WHERE pages.page_id NOT in(
  SELECT 
  page_likes.page_id
  FROM
  page_likes
  )