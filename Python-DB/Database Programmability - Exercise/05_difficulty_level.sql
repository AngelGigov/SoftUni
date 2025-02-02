CREATE OR REPLACE FUNCTION fn_difficulty_level(level INTEGER)
RETURNS VARCHAR
AS
    $$
        DECLARE

        BEGIN
            RETURN (
                CASE
                    WHEN level <= 40 THEN 'Normal Difficulty'
                    WHEN level >= 41 AND level <= 60 THEN 'Nightmare Difficulty'
                    WHEN level > 60 THEN 'Hell Difficulty'
                END
                    );
        END;

    $$

LANGUAGE plpgsql;

SELECT
    u.id as user_id,
    ug.level,
    ug.cash,
    fn_difficulty_level(ug.level) AS difficulty_level
FROM
    users AS u
JOIN
    users_games as ug
ON u.id = ug.user_id
ORDER BY user_id;
