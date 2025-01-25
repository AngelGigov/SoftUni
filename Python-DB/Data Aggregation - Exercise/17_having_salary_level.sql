SELECT
    department_id,
    COUNT(first_name) AS num_employees,
    CASE
        WHEN AVG(salary) > 50000 THEN 'Above average'
        WHEN AVG(salary) <= 50000 THEN 'Below average'
        WHEN AVG(salary) > 50000 THEN 'Above average'
    END as salary_level
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 30000
ORDER BY department_id