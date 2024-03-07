# Write your MySQL query statement below

select name,population,area from world where area>=3000000 UNION (select p.name,p.population,p.area from world p where p.population>=25000000);