/*
Enter your query here.
*/
select round(sqrt((power(min(long_w) - max(long_w) , 2)) + (power(min(lat_n) - max(lat_n), 2))), 4) from station;
