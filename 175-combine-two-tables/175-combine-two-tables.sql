# Write your MySQL query statement below
Select a.firstName, a.lastName, b.city, b.state
From Person as a
Left Join Address as b on a.personID = b.personID