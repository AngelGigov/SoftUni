 SELECT
     product_id,
     rate,
     description,
     customer_id,
     age,
     gender
 FROM
     feedbacks AS f
 JOIN
    customers AS c ON f.customer_id = c.id
 WHERE
     f.rate < 5
        AND
     (c.gender = 'F' AND c.age > 30)
 ORDER BY
     product_id DESC