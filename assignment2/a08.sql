SELECT SUM(A.count*B.count) FROM
(SELECT term, count FROM frequency WHERE docid = '10080_txt_crude' ORDER BY term) A INNER JOIN
(SELECT term, count FROM frequency WHERE docid = '17035_txt_earn' ORDER BY term) B ON A.term == B.term;