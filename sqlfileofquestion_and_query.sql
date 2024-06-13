-- Question 1) What is my income in my last 3 months.My Account Number is 409000493201'.
SELECT SUM(Deposit_amount) AS Total_Income FROM transactions
WHERE Account_No = "409000493201'" AND Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 3 MONTH);



-- Question 2) What is the total expenses of last 8 months for account number 409000611074'
SELECT SUM(Withdrawal_amount) AS Total_Expenses FROM transactions WHERE 
Account_No = "409000611074'" AND Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 8 MONTH);



-- Question 3) How much did I save last month as my account number 409000493201' 
SELECT (SUM(Deposit_amount) - SUM(Withdrawal_amount)) AS Savings_Last_Month FROM 
transactions WHERE Account_No = "409000493201'" AND YEAR(Value_date) = YEAR(CURRENT_DATE() 
- INTERVAL 1 MONTH) AND MONTH(Value_date) = MONTH(CURRENT_DATE() - INTERVAL 1 MONTH);



-- Question 4) How many transactions did I make in last 7 month as my account number 409000493201'
SELECT COUNT(*) AS Total_Transactions FROM transactions WHERE 
Account_No = "409000493201'" AND Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 MONTH);



-- Question 5) How many transactions did I make in last 2 week as my account number 409000493201'
SELECT COUNT(*) AS Total_Transactions FROM transactions WHERE Account_No = "409000493201'" AND
 Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 2 WEEK);
 
 
 
 -- Question 6) What was my total spending last week as my account number is 409000493201'
SELECT SUM(Withdrawal_amount) AS Total_Spending FROM transactions
WHERE Account_No = "409000493201'" AND Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 WEEK)
AND Value_date < CURRENT_DATE();
SELECT SUM(Withdrawal_amount) AS Total_Spending FROM transactions WHERE Account_No = "409000493201'" AND 
Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 WEEK);



 -- Question 6) How many fund transfer I did in last 30 days?
SELECT COUNT(*) AS Total_Fund_Transfers FROM transactions
WHERE Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY) ;



 -- Question 6) Can you give me a breakdown of my expenses for each day this week as my account number is  409000493201' ",
SELECT Date, SUM(Withdrawal_amount) AS Expense_Total FROM transactions WHERE Account_No = "409000493201'" AND 
Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY) GROUP BY Date;




-- ,
--     {
--         'Question':"Can you give me a breakdown of my expenses for each day this week as my account number is  409000493201' ",
--         'SQLQuery':"""SELECT Date, SUM(Withdrawal_amount) AS Expense_Total FROM transactions WHERE Account_No = "409000493201'" AND 
-- Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY) GROUP BY Date;
--         """,
--         'SQLResult':"Expense_Total = {'2024-06-09': 62112,'2024-06-10': 10331}",
--         'Answer':"Expense_Total = {'2024-06-09': 62112,'2024-06-10': 10331}"
--     }

SELECT Date, SUM(Withdrawal_amount) AS Total_Spending FROM transactions WHERE Account_No = "409000493201'" AND 
Value_date BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY) AND CURDATE() GROUP BY Date;

SELECT Date, SUM(Withdrawal_amount) AS Total_Expenses FROM transactions WHERE 
Account_No = "409000493201'" AND Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY) Group by Date;




 -- Question 7) Give me the breakdown of my expenses for each day this month as my account number is  409000493201'?
SELECT DATE(Value_date) AS Date, SUM(Withdrawal_amount) AS Total_Spending FROM transactions WHERE 
Account_No = "409000493201'" AND YEAR(Value_date) =  year(CURRENT_DATE()) AND MONTH(Value_date) = MONTH(CURRENT_DATE())
GROUP BY DATE(Value_date);



 -- Question 8) Can you give me a breakdown of my income and expenses for each day this month as my account number is  409000493201' 
SELECT Date, SUM(Deposit_amount) AS Total_income ,SUM(Withdrawal_amount) AS Total_Expenses 
FROM transactions 
WHERE Account_No = "409000493201'"
AND YEAR(Value_date) = YEAR(CURRENT_DATE())
AND MONTH(Value_date) = MONTH(CURRENT_DATE())
GROUP BY Date;







 -- Question 9) Show me a summary of my spending for the past month.&quot;
SELECT Date, SUM(Withdrawal_amount) AS Total_Spending 
FROM transactions 
WHERE Account_No = "409000493201'"
AND YEAR(Value_date) = YEAR(CURRENT_DATE() - INTERVAL 1 MONTH)
AND MONTH(Value_date) = MONTH(CURRENT_DATE() - INTERVAL 1 MONTH)
GROUP BY Date;


SELECT Date,SUM(Withdrawal_amount) AS Total_Spending 
FROM transactions 
WHERE Account_No = "409000493201'"
AND MONTH(Value_date) = MONTH(CURRENT_DATE())-1
GROUP BY Date;

SELECT Date, SUM(Withdrawal_amount) AS Total_Spending 
FROM transactions 
WHERE Account_No = "409000493201'"
AND YEAR(Value_date) = YEAR(CURRENT_DATE)
AND MONTH(Value_date) = MONTH(CURRENT_DATE) - 1
GROUP BY Date;





SELECT Date, SUM(Withdrawal_amount) AS Total_Expenses FROM transactions WHERE Account_No = "409000493201'" AND MONTH(Value_date) = LAST_MONTH(CURRENT_DATE()) GROUP BY Date;

SELECT Date, SUM(Withdrawal_amount) AS Total_Expense FROM transactions WHERE Account_No = "409000493201'" AND Value_date >= CURDATE() GROUP BY Date;

SELECT SUM(Balance_amount) AS TotalSavings FROM transactions WHERE Account_No = "409000493201'" AND YEAR(Value_date) = YEAR(CURRENT_DATE() 
- INTERVAL 1 YEAR) AND MONTH(Value_date) = MONTH(CURRENT_DATE());


 -- Question 9) What is my total saving of this year as my account number is 409000493201'
SELECT SUM(Deposit_amount)-sum(Withdrawal_amount) AS Total_Saving_This_Year FROM transactions 
WHERE Account_No = "409000493201'" AND YEAR(Value_date) = YEAR(CURRENT_DATE());


 -- Question 9)  What is my total saving of previous year as my account number is 409000493201'
SELECT (SUM(Deposit_amount) - SUM(Withdrawal_amount)) AS Total_Savings FROM transactions 
WHERE Account_No = "409000493201'" AND YEAR(Value_date) = YEAR(CURRENT_DATE - INTERVAL 1 YEAR);
SELECT (SUM(Deposit_amount) - SUM(Withdrawal_amount)) AS Total_Savings FROM transactions 
WHERE Account_No = "409000493201'" AND YEAR(Value_date) = YEAR(CURRENT_DATE())-1;




 -- Question 10)show the total savings of previous year for each month as my account number is 409000493201'

SELECT MONTH(Value_date) AS Month, (SUM(Deposit_amount) - SUM(Withdrawal_amount)) AS Total_Savings 
FROM transactions WHERE Account_No = "409000493201'" AND YEAR(Value_date) = YEAR(CURRENT_DATE - INTERVAL 1 YEAR)
GROUP BY MONTH(Value_date)
ORDER BY MONTH(Value_date);



 -- Question 11)What was my bank balance each year as my account number is 409000493201'
SELECT YEAR(Value_date) AS Year,SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Year_End_Balance
FROM transactions WHERE Account_No = "409000493201'"
GROUP BY YEAR(Value_date) ORDER BY Year;

SELECT 
    Year,
    SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Year_End_Balance
FROM (
    SELECT 
        YEAR(Value_date) AS Year,
        SUM(Deposit_amount) OVER (PARTITION BY Account_No ORDER BY Value_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS Deposit_amount,
        SUM(Withdrawal_amount) OVER (PARTITION BY Account_No ORDER BY Value_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS Withdrawal_amount
    FROM 
        transactions
    WHERE 
        Account_No = "409000493201'"
) AS Yearly_Summary
GROUP BY 
    Year
ORDER BY 
    Year;
    
    




 -- Question 12)How much amount did i save each year as my account number is  409000493201'
SELECT YEAR(Value_date) AS Year,SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Savings
FROM transactions WHERE Account_No = "409000493201'"
GROUP BY YEAR(Value_date);


 -- Question 13)How much amount did i spent each year as my account number is  409000493201'
SELECT YEAR(Value_date) AS 'Year', SUM(Withdrawal_amount) AS 'Total Spent'
FROM transactions
WHERE Account_No = "409000493201'"
GROUP BY YEAR(Value_date)
ORDER BY YEAR(Value_date);




SELECT SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Savings_Last_Two_Years FROM 
transactions WHERE Account_No = "409000493201'" AND YEAR(Value_date) In
(DATE_SUB(CURRENT_DATE(), INTERVAL 2 YEAR), CURDATE());


 -- Question 13) How much amount did i save in last 2 year as my account number is 409000611074'
SELECT YEAR(Value_date) AS Year, SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Net_Savings
FROM transactions 
WHERE Account_No = "409000611074'"
AND Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 2 YEAR)
GROUP BY YEAR(Value_date);
    


-- lllm 
SELECT SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Savings
FROM transactions WHERE Account_No = "409000493201'" AND Date > CURDATE() - INTERVAL 2 YEAR;

-- GPT 
SELECT SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Savings_Last_Two_Years
FROM transactions
WHERE Account_No = "409000493201'"
AND Date >= DATE_SUB(CURDATE(), INTERVAL 2 YEAR);



SELECT DATE(Value_date) AS Date, SUM(Withdrawal_amount) AS Total_Spending 
FROM transactions 
WHERE Account_No = "409000493201'"
AND Value_date >= DATE_SUB(CURDATE(), INTERVAL 1 WEEK) 
GROUP BY DATE(Value_date);




SELECT DATE(Value_date) AS Date, SUM(Withdrawal_amount) AS Total_Spending 
FROM transactions WHERE Account_No = "409000493201'" AND Value_date >= DATE_SUB(CURDATE(), INTERVAL 1 WEEK)
GROUP BY DATE(Value_date);




    



