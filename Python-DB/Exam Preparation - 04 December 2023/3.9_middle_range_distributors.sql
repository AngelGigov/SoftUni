SELECT
    d.name AS distributor_name,
    i.name AS ingredient_name,
    p.name AS product_name,
    AVG(f.rate)
FROM
    distributors AS d
JOIN
    ingredients AS i ON i.distributor_id = d.id
JOIN
    products_ingredients AS pi ON i.id = pi.ingredient_id
JOIN
    products AS p ON p.id = pi.product_id
JOIN
    feedbacks AS f ON p.id = f.product_id
GROUP BY d.name, i.name, p.name
HAVING
    AVG(f.rate) > 5 AND AVG(f.rate) < 8
ORDER BY
    distributor_name,
    ingredient_name,
    product_name
;
