# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below

Delete from Person 
Where Person.id = any
    (Select * from(
        Select a.id 
    from Person as a
    join Person as b
    on a.email = b.email
    where a.id > b.id
    ) as p)