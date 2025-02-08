SELECT
    CONCAT(LEFT(description, 10), '...') AS summary,
    TO_CHAR(capture_date, 'DD.MM HH24:MI') AS date
FROM photos AS p
WHERE
    extract(DAY FROM capture_date) = 10
ORDER BY
    capture_date DESC;