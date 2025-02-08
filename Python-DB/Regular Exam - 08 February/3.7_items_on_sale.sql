SELECT
    i.name,
    UPPER(b.name) || '/' || LOWER(c.name) AS promotion,
    COALESCE('On sale: ' || i.description, 'On sale: ') AS description,
    i.quantity
FROM
    items i
JOIN
    brands b ON i.brand_id = b.id
JOIN
    classifications c ON i.classification_id = c.id
WHERE
    i.id NOT IN (SELECT DISTINCT item_id FROM orders_items)
ORDER BY
    i.quantity DESC,
    i.name ASC;