# Write your MySQL query statement below
WITH CTE_s1 AS(
    SELECT DISTINCT 
        product_id,
        "store1" AS store,
        store1 AS price
    FROM Products
    WHERE store1 IS NOT NULL
),
CTE_s2 AS(
    SELECT DISTINCT 
        product_id,
        "store2" AS store,
        store2 AS price
    FROM Products
    WHERE store2 IS NOT NULL
),
CTE_s3 AS(
    SELECT DISTINCT 
        product_id,
        "store3" AS store,
        store3 AS price
    FROM Products
    WHERE store3 IS NOT NULL
)
SELECT * FROM CTE_s1 UNION
SELECT * FROM CTE_s2 UNION
SELECT * FROM CTE_s3
;