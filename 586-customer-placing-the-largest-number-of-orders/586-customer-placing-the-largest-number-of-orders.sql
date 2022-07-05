# Write your MySQL query statement below

Select a.customer_number
from Orders as a 
group by a.customer_number
order by count(a.customer_number) desc
limit 1
