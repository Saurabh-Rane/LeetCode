# Write your MySQL query statement below

Select b.name as Employee
From Employee a, Employee b
Where b.managerId = a.id 
and b.salary > a.salary