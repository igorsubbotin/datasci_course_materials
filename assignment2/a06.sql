SELECT COUNT(*) FROM
(SELECT docid, sum(c) as d FROM (SELECT docid, term, 1 as c FROM frequency WHERE term = 'transactions' OR term = 'world') GROUP BY docid HAVING d > 1);