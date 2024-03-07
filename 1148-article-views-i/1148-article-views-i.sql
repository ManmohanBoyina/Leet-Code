# Write your MySQL query statement below
select s1.author_id as id from views s1 where s1.author_id IN (select s2.author_id from views s2 where s1.author_id=s2.viewer_id) GROUP BY author_id ORDER BY author_id ASC;