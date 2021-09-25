/*
Enter your query here.
*/
select distinct city from station where city REGEXP '^[^aeiou]' and city REGEXP '[^aeiou]$';
