CREATE OR REPLACE PROCEDURE udp_modify_account(address_street VARCHAR(30), address_town VARCHAR(30))
AS
$$
BEGIN
    UPDATE accounts a
    SET job_title = CONCAT('(Remote) ', job_title)
    FROM addresses addr
    WHERE a.id = addr.account_id
    AND addr.street = address_street
    AND addr.town = address_town;

    COMMIT;
END;
$$
LANGUAGE plpgsql;