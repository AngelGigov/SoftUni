CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INT
AS
$$
    DECLARE
        count_name INT;

    BEGIN
        SELECT
            count(*)
        FROM
            employees AS e
        JOIN addresses AS a
                USING (address_id)
        JOIN towns AS t
            USING (town_id)
        WHERE t.name = town_name  INTO count_name;

        RETURN count_name;

    END

$$
LANGUAGE plpgsql;

-- SELECT fn_count_employees_by_town('Sofia')