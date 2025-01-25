SELECT
	department_id,
	AVG(salary) AS employee_count
FROM employees
GROUP BY department_id
ORDER BY department_id;