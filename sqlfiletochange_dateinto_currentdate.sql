

########################################################## ARL BANK116K FOR MANAGING THE CURRENT DATE

-- #######################################This is for Value_date column only i.e not for Date column ##################################### 

SELECT MAX(Value_date) INTO @max_date FROM transactions;
select date(@max_date) from transactions;
 -- *************************** To convert the old date into the latest date like 2024 in the format like 2024-03-12 
SELECT 
    CASE 
        WHEN DATE(Value_date) + INTERVAL (DATEDIFF(CURRENT_DATE(), @max_date)) DAY <= CURRENT_DATE() 
        THEN DATE_FORMAT(DATE(Value_date) + INTERVAL (DATEDIFF(CURRENT_DATE(), @max_date)) DAY, '%Y-%m-%d') 
        ELSE NULL 
    END AS adjusted_date
FROM 
    transactions;
    
   
-- **************************** To create a new column that will have the latest value_date instead of the old value date column 
ALTER TABLE transactions
ADD COLUMN adjusted_date DATE;

-- ************************ To store the current value_date in the table

SET SQL_SAFE_UPDATES = 0;  -- To disable the safe mode temporarily 

UPDATE transactions
SET adjusted_date = CASE 
                        WHEN DATE(Value_date) + INTERVAL (DATEDIFF(CURRENT_DATE(), @max_date)) DAY <= CURRENT_DATE() 
                        THEN DATE(Value_date) + INTERVAL (DATEDIFF(CURRENT_DATE(), @max_date)) DAY
                        ELSE NULL 
                    END
WHERE Account_No IS NOT NULL;

SET SQL_SAFE_UPDATES = 1;  -- To disable the safe mode temporarily 

-- *************************To remove the old Value_date column as it is no longer needed as there is new column of Value_date with latest column 
ALTER TABLE transactions
DROP COLUMN Value_date;

 -- *************************** To Rename the adjusted_date column back to Value_date column
 
 Alter table transactions
 Rename column adjusted_date to Value_date;
 
--  ????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????-- 
-- #######################################This is for Date column ##################################### 

SELECT MAX(Date) INTO @max_date FROM transactions;
SELECT DATE(@max_date) FROM transactions;

-- To convert the old date into the latest date like 2024 in the format like 2024-03-12
SELECT 
    CASE 
        WHEN DATE(Date) + INTERVAL (DATEDIFF(CURRENT_DATE(), @max_date)) DAY <= CURRENT_DATE() 
        THEN DATE_FORMAT(DATE(Date) + INTERVAL (DATEDIFF(CURRENT_DATE(), @max_date)) DAY, '%Y-%m-%d') 
        ELSE NULL 
    END AS adjusted_date
FROM 
    transactions;

-- To create a new column that will have the latest value_date instead of the old value date column
ALTER TABLE transactions
ADD COLUMN adjusted_date DATE;

-- To store the current value_date in the table
SET SQL_SAFE_UPDATES = 0; -- To disable the safe mode temporarily

UPDATE transactions
SET adjusted_date = CASE 
                        WHEN DATE(Date) + INTERVAL (DATEDIFF(CURRENT_DATE(), @max_date)) DAY <= CURRENT_DATE() 
                        THEN DATE(Date) + INTERVAL (DATEDIFF(CURRENT_DATE(), @max_date)) DAY
                        ELSE NULL 
                    END
WHERE Account_No IS NOT NULL;

SET SQL_SAFE_UPDATES = 1; -- To disable the safe mode temporarily

-- To remove the old Value_date column as it is no longer needed as there is new column of Value_date with latest column
ALTER TABLE transactions
DROP COLUMN Date;

-- To rename the adjusted_date column back to Value_date column
ALTER TABLE transactions
RENAME COLUMN adjusted_date TO Date;
