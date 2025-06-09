# Write your MySQL query statement below
WITH CTE_Stocks AS(
    SELECT stock_name,
        SUM(CASE WHEN operation = "Buy" THEN price ELSE 0 END) AS total_buy,
        SUM(CASE WHEN operation = "Sell" THEN price ELSE 0 END) AS total_sell
    FROM Stocks
    GROUP BY stock_name
)
SELECT DISTINCT stock_name, (total_sell - total_buy) AS capital_gain_loss
FROM CTE_Stocks
;