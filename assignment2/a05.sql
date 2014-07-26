SELECT COUNT(*) FROM 
(SELECT docid, sum(count) words FROM frequency GROUP BY docid HAVING words > 300);