# Write your MySQL query statement below

Select distinct a.email
From Person as a 
Inner Join Person as b
on a.email = b.email 
Where a.id != b.id