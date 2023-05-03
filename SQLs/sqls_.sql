




-- # SQL QUESTION 2
select 
he.department_id ,
d.department ,
j.job,
(select
count(*)
from hired_employees he_inner
where 
he.datetime BETWEEN '2021-01-01' and '2021-03-31'
and he.department_id = he_inner .department_id 
and he.job_id = he_inner.job_id 
GROUP by department_id ,job_id ) as 'Q1',
(select
count(*)
from hired_employees he_inner
where 
he.datetime BETWEEN '2021-04-01' and '2021-06-30'
and he.department_id = he_inner .department_id 
and he.job_id = he_inner.job_id 
GROUP by department_id ,job_id ) as 'Q2',
(select
count(*)
from hired_employees he_inner
where 
he.datetime BETWEEN '2021-07-01' and '2021-09-30'
and he.department_id = he_inner .department_id 
and he.job_id = he_inner.job_id 
GROUP by department_id ,job_id ) as 'Q3',
(select
count(*)
from hired_employees he_inner
where 
he.datetime BETWEEN '2021-10-01' and '2021-12-31'
and he.department_id = he_inner .department_id 
and he.job_id = he_inner.job_id 
GROUP by department_id ,job_id )  as 'Q4'
from hired_employees he 
inner join departments d  on he.department_id = d.id
inner join jobs j on he.job_id = j.id 
group by department_id ,job_id 
order by d.department , j.job  ASC ;