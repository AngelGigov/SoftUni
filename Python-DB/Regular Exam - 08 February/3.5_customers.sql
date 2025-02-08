SELECT
    id,
    last_name,
    loyalty_card
FROM
    customers
WHERE
    loyalty_card
    AND
    LOWER(last_name) LIKE '%m%'
ORDER BY
    last_name DESC,
    id
;