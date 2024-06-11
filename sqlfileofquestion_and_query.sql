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











