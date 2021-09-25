/*
Enter your query here.
*/
select max(salary*months), count(*) from employee where salary*months = (select max(salary*months) from employee);
