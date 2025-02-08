SELECT
    CONCAT_WS(' ', first_name, last_name) as full_name,
    concat(LOWER(LEFT(first_name, 1)), RIGHT(last_name, 2), length(last_name), '@sm-cast.com') as email,
    awards
FROM
    actors AS a
LEFT JOIN
    productions_actors AS pa ON a.id = pa.actor_id
LEFT JOIN
    productions AS p on p.id = pa.production_id
WHERE
    production_id IS NULL
ORDER BY
    awards DESC,
    a.id