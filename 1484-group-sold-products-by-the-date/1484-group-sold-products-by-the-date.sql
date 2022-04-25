# Write your MySQL query statement below
SELECT sell_date, COUNT(DISTINCT product) AS num_sold, GROUP_CONCAT(DISTINCT product ORDER BY product) AS Products
FROM Activities
GROUP BY sell_date;



