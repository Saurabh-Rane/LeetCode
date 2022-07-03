# Write your MySQL query statement below
Select Customers.name as Customers
from Customers
where id != all
    (Select a.id 
    from Customers as a
    inner join Orders as b
    on a.id = b.customerID)