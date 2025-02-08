SELECT
--     *
    c.name AS country_name,
    count(*) AS productions_count,
    COALESCE(AVG(pi.budget), 0) AS avg_budget
FROM
    countries AS c
JOIN
    productions AS p ON c.id = p.country_id
JOIN
    productions_info AS pi ON pi.id = p.production_info_id
GROUP BY c.name
HAVING count(c.id) > 0
ORDER BY
    productions_count DESC,
    country_name ASC;

