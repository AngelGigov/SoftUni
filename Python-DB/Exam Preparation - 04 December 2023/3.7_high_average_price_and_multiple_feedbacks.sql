 SELECT
     p.name AS product_name,
     ROUND(AVG(price), 2) as average_price,
     count(f.id) as total_feedbacks
 FROM
     products AS p
 JOIN
    feedbacks AS f ON f.product_id = p.id
 WHERE
     price > 15
GROUP BY p.name
HAVING count(f.id) > 1
ORDER BY
    total_feedbacks,
    average_price DESC

