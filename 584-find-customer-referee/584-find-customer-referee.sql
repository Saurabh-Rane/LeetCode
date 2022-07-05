# Write your MySQL query statement below

Select Customer.name 
from Customer
where Customer.referee_id != 2 
    or Customer.referee_id is NULL