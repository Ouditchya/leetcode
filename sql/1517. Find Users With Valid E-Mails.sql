SELECT *
-- ,REGEXP_LIKE(mail, '^[A-Za-z]+[A-Za-z0-9._-]+@leetcode+[.]+com') as c1
-- ,REGEXP_LIKE(mail, '^[A-Za-z]+@leetcode+[.]+com') as c2
FROM Users 
WHERE 1 = 1
    AND mail LIKE '%leetcode.com'
    AND (REGEXP_LIKE(mail, '^[A-Za-z]+[A-Za-z0-9._-]+@leetcode+[.]+com')
        OR REGEXP_LIKE(mail, '^[A-Za-z]+@leetcode+[.]+com'))
;