SELECT
    last_name,
    count(notes)
FROM
    wizard_deposits
WHERE notes LIKE '%Dumbledore%'
group by last_name