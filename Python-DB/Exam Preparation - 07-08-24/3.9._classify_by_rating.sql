SELECT
    p.title,
    CASE
        WHEN pi.rating <= 3.5 THEN 'poor'
        WHEN pi.rating > 8 THEN 'excelent'
        ELSE 'good'
    END AS rating,
    CASE
        WHEN pi.has_subtitles THEN 'Bulgarian'
        ELSE 'N/A'
    END AS subtitles,
    count(pa.actor_id) AS actors_count
FROM
    productions p
JOIN
    productions_info pi ON p.production_info_id = pi.id
LEFT JOIN
    productions_actors pa ON p.id = pa.production_id
GROUP BY
    p.title,
    pi.rating,
    pi.has_subtitles
ORDER BY
    rating,
    actors_count DESC,
    p.title
