# Challenge one

SELECT a.au_id, a.au_lname, a.au_fname, t.title, p.pub_name
FROM publications.authors as a
inner JOIN publications.titleauthor as tau
ON a.au_id = tau.au_id
inner JOIN publications.titles as t
ON tau.title_id = t.title_id
inner JOIN publications.publishers as p
ON t.pub_id = p.pub_id;

# Challenge two

Select AU_ID, LAST_NAME, FIRST_NAME, PUBLISHER, count(distinct(titles)) FROM
(SELECT a.au_id AS AU_ID, a.au_lname LAST_NAME, a.au_fname FIRST_NAME, t.title as titles, p.pub_name as PUBLISHER
FROM publications.authors as a
inner JOIN publications.titleauthor as tau
ON a.au_id = tau.au_id
inner JOIN publications.titles as t
ON tau.title_id = t.title_id
inner JOIN publications.publishers as p
ON t.pub_id = p.pub_id) pru
group by PUBLISHER, AU_ID
;
