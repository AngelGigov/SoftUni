SELECT
    id,
    TO_CHAR(created_at, 'DD-MM-YYYY') AS created_at,
    customer_id
FROM
    orders
WHERE
    TO_CHAR(created_at, 'DD-MM-YYYY') > '01-01-2025'::VARCHAR
    AND customer_id BETWEEN 15 AND 30
ORDER BY
    TO_CHAR(created_at, 'DD-MM-YYYY') ASC,
    customer_id DESC,
    id ASC
LIMIT 5;