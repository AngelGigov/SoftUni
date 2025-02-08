CREATE TABLE IF NOT EXISTS gift_recipients (
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    country_id INT NOT NULL,
    gift_set BOOLEAN DEFAULT FALSE
);

INSERT INTO gift_recipients (
    "name",
    country_id,
    gift_set
)
SELECT
    concat(first_name, ' ', last_name) as "name",
    country_id AS "country_id",
    CASE
        WHEN country_id IN (7, 8, 14, 17, 26) THEN TRUE
        ELSE FALSE
    END AS gift_sent
FROM
    customers;
