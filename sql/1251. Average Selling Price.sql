WITH CTE_combined AS(
    SELECT p.*, q.purchase_date, COALESCE(q.units, 0) as units
    FROM Prices p
        LEFT JOIN UnitsSold q
            ON p.product_id = q.product_id
                AND q.purchase_date BETWEEN p.start_date AND p.end_date
)
SELECT product_id, COALESCE(ROUND(SUM(price * units)/ SUM(units), 2), 0) AS average_price
FROM CTE_combined
GROUP BY 1
;