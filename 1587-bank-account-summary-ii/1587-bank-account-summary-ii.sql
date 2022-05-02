# Write your MySQL query statement below
SELECT name, SUM(amount) AS balance
FROM Users
JOIN transactions USING(account)
GROUP BY account
HAVING balance > 10000;