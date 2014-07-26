SELECT A.term, A.count, B.term, B.count, A.count*B.count FROM
(SELECT term, SUM(count) count FROM frequency WHERE docid = '10080_txt_crude' GROUP BY term) A INNER JOIN
(SELECT term, SUM(count) count FROM frequency WHERE docid = '17035_txt_earn' GROUP BY term) B ON A.term == B.term;