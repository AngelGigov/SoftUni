SELECT
    country_code,
    count(mountain_range)
FROM
    mountains AS m
LEFT JOIN
        mountains_countries AS mc
ON
    m.id = mc.mountain_id
WHERE country_code IN ('US', 'RU', 'BG')
GROUP BY country_code
ORDER BY count(mountain_range) DESC;