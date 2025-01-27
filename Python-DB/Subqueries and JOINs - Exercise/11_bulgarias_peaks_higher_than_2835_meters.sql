SELECT mc.country_code,
       m.mountain_range,
       p.peak_name,
       p.elevation
FROM peaks AS p
         LEFT JOIN mountains AS m
                   ON p.mountain_id = m.id
         JOIN mountains_countries AS mc
              ON mc.mountain_id = m.id
WHERE country_code = 'BG'
AND elevation > '2835'
ORDER BY elevation DESC;