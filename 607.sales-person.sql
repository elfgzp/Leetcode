# Write your MySQL query statement below

SELECT
    `name` 
FROM 
`salesperson` 
WHERE `sales_id` NOT IN (
SELECT
    `orders`.`sales_id`
FROM (
    SELECT
        `com_id`
    FROM 
        `company` 
    WHERE `name` = 'RED'
) `com` INNER JOIN `orders` ON `com`.`com_id` = `orders`.`com_id`
) 

