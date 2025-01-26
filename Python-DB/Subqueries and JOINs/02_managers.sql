SELECT
    e.employee_id,
    CONCAT(e.first_name, ' ', e.last_name),
    d.department_id,
    d.name as department_name
FROM employees AS e
RIGHT JOIN departments AS d
ON d.manager_id = e.employee_id
ORDER BY employee_id
LIMIT 5;