CREATE OR REPLACE PROCEDURE sp_customer_country_name(
    IN customer_full_name VARCHAR(50),
    OUT country_name VARCHAR(50)
)
AS
    $$

    BEGIN

        country_name := (
            SELECT
                co.name
            FROM
                customers AS c
            JOIN
                countries AS co ON c.country_id = co.id
            WHERE
                concat(first_name, ' ', last_name) = customer_full_name
        );

    END;

    $$
LANGUAGE plpgsql;