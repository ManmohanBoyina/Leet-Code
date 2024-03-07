# Write your MySQL query statement below
SELECT COALESCE(u.unique_id, NULL) as unique_id,e.name as name
FROM Employees e
LEFT JOIN EmployeeUNI u ON e.id = u.id;
