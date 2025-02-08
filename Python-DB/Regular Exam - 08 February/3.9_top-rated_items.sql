SELECT
    i.name AS item_name,
    ROUND(AVG(r.rating), 2) AS average_rating,
    COUNT(r.rating) AS total_reviews,
    b.name AS brand_name,
    c.name AS classification_name
FROM reviews r
JOIN items i ON r.item_id = i.id
JOIN brands b ON i.brand_id = b.id
JOIN classifications c ON i.classification_id = c.id
GROUP BY i.id, i.name, b.name, c.name
HAVING COUNT(r.rating) >= 3
ORDER BY average_rating DESC, item_name ASC
LIMIT 3;