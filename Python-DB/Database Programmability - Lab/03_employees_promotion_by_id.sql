CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id(id INT)
AS
    $$
        BEGIN

            IF (SELECT count(*) FROM employees WHERE employee_id = id) != 1 THEN
                ROLLBACK ;
            ELSE
            UPDATE employees
            SET salary = salary * 1.05
            WHERE employee_id = id;
            END IF;
            COMMIT;
        END
    $$
LANGUAGE plpgsql;