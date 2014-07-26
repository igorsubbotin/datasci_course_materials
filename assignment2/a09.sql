SELECT F.docid, SUM(F.count*Q.count) score FROM
((SELECT * FROM frequency) F INNER JOIN
(SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count) Q ON F.term == Q.term)
GROUP BY F.docid
ORDER BY score DESC LIMIT 10;