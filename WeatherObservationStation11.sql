/*
Enter your query here.
*/
select distinct city from station where city REGEXP '^[^aeiou]' or city REGEXP '[^aeiou]$';
