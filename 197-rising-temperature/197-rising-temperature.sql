# Write your MySQL query statement below

Select a.id as Id
from Weather as a
join weather as b
on datediff(a.recordDate, b.recordDate) = 1
and a.temperature > b.temperature
