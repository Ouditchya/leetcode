SELECT t1.firstName, t1.lastName,
    CASE WHEN t2.city IS NULL then NULL ELSE t2.city END AS city,
    CASE WHEN t2.state IS NULL then NULL ELSE t2.state END AS state
FROM Person t1
    LEFT JOIN Address t2
        ON t1.personId = t2.personId
;