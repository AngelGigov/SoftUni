SELECT
    p.id as photo_id,
    (SELECT COUNT(*) FROM likes WHERE photo_id = p.id) AS likes,
    (SELECT COUNT(*) FROM comments WHERE photo_id = p.id) AS comments
FROM
    photos AS p
GROUP BY
    p.id
ORDER BY likes DESC, comments DESC, p.id;