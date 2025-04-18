SELECT CASE WHEN e.id = eu.id THEN eu.unique_id ELSE NULL END AS unique_id,
e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu
ON e.id = eu.id;