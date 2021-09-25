/*
Enter your query here.
*/
select round(abs(min(LAT_N)-max(LAT_N))+abs(min(long_w)- max(long_w)),4) from STATION;
