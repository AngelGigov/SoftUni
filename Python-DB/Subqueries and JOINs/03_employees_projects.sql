SELECT
    e.employee_id,
    concat(e.first_name, ' ', e.last_name) AS full_name,
    p.project_id,
    p.name as project_name
FROM employees AS e
LEFT JOIN employees_projects AS ep USING (employee_id)
LEFT JOIN projects AS p USING (project_id)
WHERE project_id = 1
;