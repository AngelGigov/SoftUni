SELECT
	department_id,
	MIN(salary) AS employee_count
FROM employees
GROUP BY department_id
ORDER BY department_id;