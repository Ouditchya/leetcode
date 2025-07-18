# Write your MySQL query statement below
SELECT t1.name, SUM(t2.amount) AS balance
FROM Users t1
    JOIN Transactions t2
        ON t1.account = t2.account
GROUP BY t1.name
HAVING balance > 10000
;