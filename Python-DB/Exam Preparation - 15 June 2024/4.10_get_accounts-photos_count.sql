CREATE OR REPLACE FUNCTION udf_accounts_photos_count(account_username VARCHAR(30))
RETURNS INTEGER
AS
    $$
    DECLARE

    BEGIN
        RETURN
        (SELECT
            count(*)
        FROM
            photos AS p
        JOIN
            accounts_photos AS ap ON p.id = ap.photo_id
        JOIN
            accounts AS a ON ap.account_id = a.id
        WHERE
            username = account_username
        );
    END;
    $$
LANGUAGE plpgsql;


SELECT udf_accounts_photos_count('ssantryd')

