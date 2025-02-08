CREATE OR REPLACE FUNCTION fn_feedbacks_for_product(product_name VARCHAR(25))
RETURNS TABLE(
    customer_id INT,
    customer_name VARCHAR(75),
    feedback_description VARCHAR(255),
    feedback_rate NUMERIC(4,2)
)
AS
    $$
        DECLARE

        BEGIN
            RETURN QUERY (
                SELECT
                    c.id as customer_id,
                    c.first_name as customer_name,
                    f.description as feedback_description,
                    f.rate as feedback_rate
                FROM
                    products AS p
                JOIN
                    feedbacks AS f ON p.id = f.product_id
                JOIN
                    customers AS c ON f.customer_id = c.id
                WHERE
                    p.name = product_name
                ORDER BY
                    c.id
            );

        END;

    $$
LANGUAGE plpgsql;