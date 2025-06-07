WITH cte_employees AS (
  SELECT employee_id, first_name, last_name, department_id
  FROM employees
)
SELECT *
FROM cte_employees
WHERE department_id = 50;