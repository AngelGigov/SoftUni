SELECT
	*
	-- id,
	-- first_name || ' ' || last_name AS "full_name",
	-- job_title,
	-- salary
FROM
	employees
WHERE
	salary > 1000.00
AND
	department_id = '4'