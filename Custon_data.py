#Few_shorts

few_shots=[
    {
        'Question':" Income of last 3 months. ?",
        'SQLQuery':"""SELECT SUM(Deposit_amount) AS Total_Income FROM transactions WHERE Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 3 MONTH) """,
        'SQLResult':"1530205868",
        'Answer':"1530205868 is the income of last 3 months."
    }
    ,

    {
        'Question':"Total expenses/spendings of last 8 months ?",
        'SQLQuery':"""SELECT SUM(Withdrawal_amount) AS Total_Expenses FROM transactions WHERE Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 8 MONTH) """,
        'SQLResult':"11274528407",
        'Answer':"11274528407 is the total expenses of last 8 months."
    }
    ,
      {
        'Question':"Total saving of last month as my account number is 409000493201'  ?",
        'SQLQuery':"""SELECT (SUM(Deposit_amount) - SUM(Withdrawal_amount)) AS Savings_Last_Month FROM
transactions WHERE Account_No = "409000493201'" AND YEAR(Value_date) = YEAR(CURRENT_DATE()
- INTERVAL 1 MONTH) AND MONTH(Value_date) = MONTH(CURRENT_DATE() - INTERVAL 1 MONTH);
        """,
        'SQLResult':"-193509",
        'Answer':"You lost -193509 last month."
    }
,
    {
        'Question':"How many transactions did I make in last 2 week  ",
        'SQLQuery':"""SELECT COUNT(*) AS Total_Transactions FROM transactions WHERE Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 2 WEEK) """,
        'SQLResult':"162",
        'Answer':"You made 162 transactions in last 2 week."
    },
     {
        'Question':"Amount spent last week ",
        'SQLQuery':"""SELECT SUM(Withdrawal_amount) AS Total_Spending FROM transactions WHERE Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 WEEK) """,
        'SQLResult':"",
        'Answer':"0 is your total spending last week."
    }
    , {
        'Question': "Expenses for each day this month ?",
        'SQLQuery': """SELECT Date, SUM(Withdrawal_amount) AS Total_Expenses FROM transactions WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) AND MONTH(Value_date) = MONTH(CURRENT_DATE()) GROUP BY Date """,
        'SQLResult':
        """
Date                        Total_Expenses
2024-06-02                   183648
2024-06-03                   80666
2024-06-04                   135504
2024-06-05                   92031
2024-06-06                   118475
2024-06-07                   16440
2024-06-09                   62112
2024-06-10                   10331
"""
        ,
        'Answer': """The total_expenses is 183648,80666,135504,92031,118475,16440,62112,10331 for the year 2024 month of 6 and date 02,03,04,05,06,07,09 and 10.  """
    },
    {
        'Question':"savings of previous year for each month ",
        'SQLQuery':"""SELECT MONTH(Value_date) AS Month, (SUM(Deposit_amount) - SUM(Withdrawal_amount)) AS Total_Savings FROM transactions WHERE YEAR(Value_date) = YEAR(CURRENT_DATE() - INTERVAL 1 YEAR) GROUP BY MONTH(Value_date) ORDER BY MONTH(Value_date) """,
        'SQLResult':"""
        Date                Total_Expenses
        1                       -311244
        2                          9101
        3                         3476
        4                       -15971
        5                       322249
        6                       -172560
        7                       361471
        8                       -446844
        9                       93215
        10                      -73917
        11                      294502
        12                      -404028""",
        'Answer':"Month-1:-311244, Month-2:9101, Month-3:3476"
    },
     {
        'Question':"Amount Saved each year",
        'SQLQuery':"""SELECT YEAR(Value_date) AS Year,SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Savings FROM transactions GROUP BY YEAR(Value_date) """,
        'SQLResult':"""
        Year                Savings
        2021                 497766
        2022                 272458
        2023                 -340550
        2024                 -148114
       """,
        'Answer':"You saved 497766 in 2021 ,272458 in 2022, -340550 in 2023 and -148114 in 2024."
    }
    ,
     {
        'Question':"Savings of last 2 year  ",
        'SQLQuery':"""SELECT YEAR(Value_date) AS Year, SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Net_Savings FROM transactions WHERE Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 2 YEAR) GROUP BY YEAR(Value_date) """,
        'SQLResult':"""
        Year                Savings
        2022                 2270453
        2023                 -895783
        2024                 -912470
        """,
        'Answer':"You saved 2270453 in 2022, -89578 in 2023 and -912470 in 2024."
    }
    ,
     {
        'Question':"Expenses of each day of last week  ",
        'SQLQuery':"""SELECT DATE(Value_date) AS Date, SUM(Withdrawal_amount) AS Total_Spending FROM transactions WHERE Value_date >= DATE_SUB(CURDATE(), INTERVAL 1 WEEK) GROUP BY DATE(Value_date) """,
        'SQLResult':"""
        Year                Savings
        2024-06-06           118475
        2024-06-07           16440
        2024-06-09           62112
        2024-06-10           10331

        """,
        'Answer':"You spend 118475,16440,62112,10331."
    },
    {
        'Question':"Amount spent this year ?",
        'SQLQuery':"""SELECT year(Value_date) as Year,sum(Withdrawal_amount) AS Total_Expenses FROM transactions WHERE year(Value_date) = year(curdate()) group by year(Value_date) """,
        'SQLResult':"""
        Year                Total_Expenses
       2024                    6527128485
        """,
        'Answer':"You spent 36616174 this year."
    },
    {
        'Question':"amount/money saved each month previous year ?",
        'SQLQuery':"""SELECT YEAR(Value_date) AS Year, MONTH(Value_date) AS Month, SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Savings FROM transactions WHERE YEAR(Value_date) = YEAR(CURRENT_DATE - INTERVAL 1 YEAR) GROUP BY YEAR(Value_date), MONTH(Value_date) """,
        'SQLResult':"""
        Year            Month              Savings
       2023              1                  -311244
       2023             2                       9101
       2023             3                       3476
       2023             4                       -15971
       2023             5                       322249
       2023             6                       -172560
        2023             7                   361471
       2023             8                       -446844
       2023             9                       93215
       2023             10                       -73917
       2023            11                       294502
       2023             12                       -404028
        """,
        'Answer':"You lost 311244 in month 1 ,saved 9101,3476 in month 2 and month 3  previous year."
    }
     ,
      {
        'Question':"income of the previous year ",
        'SQLQuery':"""SELECT SUM(Deposit_amount) AS Total_Income FROM transactions WHERE YEAR(Value_date) = YEAR(CURRENT_DATE) - 1 """,
        'SQLResult':"38593214103",
        'Answer':"Your income previous ysear was 38593214103."
    }
    ,
      {
        'Question':"income of the first 4 month of previous year ",
        'SQLQuery':"""SELECT SUM(Deposit_amount) AS Total_Income FROM transactions WHERE MONTH(Value_date) IN (1,2,3,4) AND YEAR(Value_date) = YEAR(CURRENT_DATE) - 1 """,
        'SQLResult':"17847505444",
        'Answer':"Your income of first 4 month of previous year was 17847505444."
    },
    {
    'Question': "amount I lost each year?",
    'SQLQuery': """
                SELECT YEAR(Value_date) AS Year,SUM(Withdrawal_amount) - SUM(Deposit_amount) AS Losses
                FROM transactions
                GROUP BY YEAR(Value_date);
                """,
    'SQLResult': """[
        (2022, Decimal('211175202')),
        (2023, Decimal('575324140')),
        (2024, Decimal('490771857')),
        (2021, Decimal('906602921')),
        (2020, Decimal('1076993185'))

    ]"""
    ,
    'Answer': "You lost 497766 in 2021, 272458 in 2022, -340550 in 2023, and -148114 in 2024."
}
  ,
    {
        'Question': "What is the average of last 5 transactions?",
        'SQLQuery': """SELECT AVG(CASE WHEN Withdrawal_amount IS NOT NULL THEN Withdrawal_amount ELSE Deposit_amount END) AS Average_Amount FROM (SELECT Withdrawal_amount, Deposit_amount FROM transactions ORDER BY Date DESC LIMIT 5) AS Last5Transactions"""
    },
    {
        'Question': "What is my total income this year?",
        'SQLQuery': """SELECT SUM(Deposit_amount) AS Total_Income FROM transactions WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
    },
    {
        'Question': "What is my income of the first 3 months of this year?",
        'SQLQuery': """SELECT SUM(Deposit_amount) AS Total_Income FROM transactions WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) AND MONTH(Value_date) IN (1, 2, 3)"""
    },
    {
        'Question': "What is my expenses of the first 4 months of this year?",
        'SQLQuery': """SELECT SUM(Withdrawal_amount) AS Total_Expenses FROM transactions WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) AND MONTH(Value_date) IN (1, 2, 3, 4)"""
    },
    {
        'Question': "What is my income of the last 5 months of this year?",
        'SQLQuery': """SELECT SUM(Deposit_amount) AS Total_Income FROM transactions WHERE Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 5 MONTH)"""
    },
    {
        'Question': "How much amount did I earn each year?",
        'SQLQuery': """SELECT YEAR(Value_date) AS Year, SUM(Deposit_amount) AS Total_Income FROM transactions GROUP BY YEAR(Value_date)"""
    }
,
    {
        'Question': "How much amount did I save each year?",
        'SQLQuery': """SELECT YEAR(Value_date) AS Year, SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Savings FROM transactions GROUP BY YEAR(Value_date)"""
    },
    {
        'Question': "How much amount did I spend each year?",
        'SQLQuery': """SELECT YEAR(Value_date) AS Year, SUM(Withdrawal_amount) AS Total_Spending FROM transactions GROUP BY YEAR(Value_date)"""
    },
    {
        'Question': "Give me the breakdown of expenses of each day of this week?",
        'SQLQuery': """SELECT DATE(Value_date) AS Date, SUM(Withdrawal_amount) AS Total_Expenses FROM transactions WHERE Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 WEEK) GROUP BY DATE(Value_date)"""
    },
    {
        'Question': "Give me the breakdown of savings of each day of this month?",
        'SQLQuery': """SELECT DATE(Value_date) AS Date, SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Daily_Savings FROM transactions WHERE MONTH(Value_date) = MONTH(CURRENT_DATE()) AND YEAR(Value_date) = YEAR(CURRENT_DATE()) GROUP BY DATE(Value_date)"""
    },
    {
        'Question': "Give me the breakdown of amount I spent each day of this month?",
        'SQLQuery': """SELECT DATE(Value_date) AS Date, SUM(Withdrawal_amount) AS Daily_Spending FROM transactions WHERE MONTH(Value_date) = MONTH(CURRENT_DATE()) AND YEAR(Value_date) = YEAR(CURRENT_DATE()) GROUP BY DATE(Value_date)"""
    },
    {
        'Question': "Give me the breakdown of amount I spent each day of this week?",
        'SQLQuery': """SELECT DATE(Value_date) AS Date, SUM(Withdrawal_amount) AS Daily_Spending FROM transactions WHERE Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 WEEK) GROUP BY DATE(Value_date)"""
    },
    {
        'Question': "On average how much amount I spent each day?",
        'SQLQuery': """SELECT AVG(Withdrawal_amount) AS Average_Daily_Spending FROM transactions"""
    },
    {
        'Question': "On average how much amount I spent each month?",
        'SQLQuery': """SELECT YEAR(Value_date) AS Year, MONTH(Value_date) AS Month, AVG(SUM(Withdrawal_amount)) OVER (PARTITION BY YEAR(Value_date), MONTH(Value_date)) AS Average_Monthly_Spending FROM transactions GROUP BY YEAR(Value_date), MONTH(Value_date)"""
    },
    {
        'Question': "On average how much amount I spent each year?",
        'SQLQuery': """SELECT YEAR(Value_date) AS Year, AVG(SUM(Withdrawal_amount)) OVER (PARTITION BY YEAR(Value_date)) AS Average_Yearly_Spending FROM transactions GROUP BY YEAR(Value_date)"""
    },
    {
        'Question': "How many transactions did I make this year?",
        'SQLQuery': """SELECT COUNT(*) AS Total_Transactions FROM transactions WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
    },
    {
        'Question': "How many transactions did I make each year?",
        'SQLQuery': """SELECT YEAR(Value_date) AS Year, COUNT(*) AS Total_Transactions FROM transactions GROUP BY YEAR(Value_date)"""
    },
    {
        'Question': "How many transactions did I make this week?",
        'SQLQuery': """SELECT COUNT(*) AS Total_Transactions FROM transactions WHERE WEEK(Value_date) = WEEK(CURRENT_DATE()) AND YEAR(Value_date) = YEAR(CURRENT_DATE())"""
    },
    {
        'Question': "How many transactions did I make this month?",
        'SQLQuery': """SELECT COUNT(*) AS Total_Transactions FROM transactions WHERE MONTH(Value_date) = MONTH(CURRENT_DATE()) AND YEAR(Value_date) = YEAR(CURRENT_DATE())"""
    },

    {
        'Question': "What is my total savings of last month?",
        'SQLQuery': """SELECT SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Total_Savings FROM transactions WHERE YEAR(Value_date) = YEAR(CURRENT_DATE - INTERVAL 1 MONTH) AND MONTH(Value_date) = MONTH(CURRENT_DATE - INTERVAL 1 MONTH)"""
    },
    {
        'Question': "What is my total savings of each year?",
        'SQLQuery': """SELECT YEAR(Value_date) AS Year, SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Total_Savings FROM transactions GROUP BY YEAR(Value_date)"""
    },
    {
        'Question': "What is my savings this week?",
        'SQLQuery': """SELECT SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Total_Savings FROM transactions WHERE WEEK(Value_date) = WEEK(CURRENT_DATE()) AND YEAR(Value_date) = YEAR(CURRENT_DATE())"""
    },
    {
        'Question': "What is my expenses amount of last month?",
        'SQLQuery': """SELECT SUM(Withdrawal_amount) AS Total_Expenses FROM transactions WHERE YEAR(Value_date) = YEAR(CURRENT_DATE - INTERVAL 1 MONTH) AND MONTH(Value_date) = MONTH(CURRENT_DATE - INTERVAL 1 MONTH)"""
    },
    {
        'Question': "What is my expenses amount of this month?",
        'SQLQuery': """SELECT SUM(Withdrawal_amount) AS Total_Expenses FROM transactions WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) AND MONTH(Value_date) = MONTH(CURRENT_DATE())"""
    },
    {
    'Question': "What is the pattern in my last 3 transactions? Are they increasing or decreasing?",
    'SQLQuery': """SELECT Transaction_details, Withdrawal_amount, Deposit_amount, Value_date
                   FROM transactions
                   ORDER BY Value_date DESC
                   LIMIT 3"""
}
,{
    'Question': "What is my current net worth?",
    'SQLQuery': """SELECT Balance_amount AS Current_Net_Worth
                   FROM transactions
                   ORDER BY Value_date DESC
                   LIMIT 1"""
},
{
    'Question': "Has my income changed recently?",
    'SQLQuery': """SELECT
                       DATE(Value_date) AS Date,
                       SUM(Deposit_amount) AS Daily_Income
                   FROM transactions
                   GROUP BY DATE(Value_date)
                   ORDER BY DATE(Value_date) DESC
                   LIMIT 7"""
}
,{
    'Question': "What is my income of the last 2 years?",
    'SQLQuery': """SELECT YEAR(Value_date) AS Year, SUM(Deposit_amount) AS Total_Income
                   FROM transactions
                   WHERE Value_date >= DATE_SUB(CURDATE(), INTERVAL 2 YEAR)
                   GROUP BY YEAR(Value_date)"""
},
{
    'Question': "What is my expenses of the last 1 year?",
    'SQLQuery': """SELECT YEAR(Value_date) AS Year, SUM(Withdrawal_amount) AS Total_Expenses
                   FROM transactions
                   WHERE Value_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
                   GROUP BY YEAR(Value_date)"""
},
{
    'Question': "What is my savings of the last 3 years?",
    'SQLQuery': """SELECT YEAR(Value_date) AS Year, SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Net_Savings
                   FROM transactions
                   WHERE Value_date >= DATE_SUB(CURDATE(), INTERVAL 3 YEAR)
                   GROUP BY YEAR(Value_date)"""
},
    {
    'Question': "Give me the income of the first 7 months of this year",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, SUM(Deposit_amount) AS Total_Income 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   AND MONTH(Value_date) <= 7 
                   GROUP BY MONTH(Value_date)"""
},
{
    'Question': "Tell me the expenses of the first 9 months of this year",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, SUM(Withdrawal_amount) AS Total_Expenses 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   AND MONTH(Value_date) <= 9 
                   GROUP BY MONTH(Value_date)"""
},
{
    'Question': "Tell me the income of the last 8 months of this year",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, SUM(Deposit_amount) AS Total_Income 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   AND MONTH(Value_date) >= (MONTH(CURRENT_DATE()) - 7)
                   GROUP BY MONTH(Value_date)"""
},
{
    'Question': "What is my average spendings each month in this year",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, AVG(Withdrawal_amount) AS Average_Spending 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY MONTH(Value_date)"""
},
{
    'Question': "Give me the average spendings of mine each month in previous year",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, AVG(Withdrawal_amount) AS Average_Spending 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) - 1
                   GROUP BY MONTH(Value_date)"""
},
{
    'Question': "Give me the average spendings of mine each month in year 2022",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, AVG(Withdrawal_amount) AS Average_Spending 
                   FROM transactions 
                   WHERE YEAR(Value_date) = 2022 
                   GROUP BY MONTH(Value_date)"""
},
{
    'Question': "What is my average spendings each week in this month",
    'SQLQuery': """SELECT WEEK(Value_date) AS Week, AVG(Withdrawal_amount) AS Average_Spending 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   AND MONTH(Value_date) = MONTH(CURRENT_DATE()) 
                   GROUP BY WEEK(Value_date)"""
},
{
    'Question': "What is my average spendings each week previous month",
    'SQLQuery': """SELECT WEEK(Value_date) AS Week, AVG(Withdrawal_amount) AS Average_Spending 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   AND MONTH(Value_date) = MONTH(CURRENT_DATE()) - 1
                   GROUP BY WEEK(Value_date)"""
},
{
    'Question': "What is my average earning each month in this year?",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, AVG(Deposit_amount) AS Average_Earning 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY MONTH(Value_date)"""
},
{
    'Question': "Tell me the earnings each month in the previous year",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, SUM(Deposit_amount) AS Total_Earnings 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) - 1
                   GROUP BY MONTH(Value_date)"""
},
{
    'Question': "What is my earnings each month in the year 2018?",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, SUM(Deposit_amount) AS Total_Earnings 
                   FROM transactions 
                   WHERE YEAR(Value_date) = 2018 
                   GROUP BY MONTH(Value_date)"""
},
{
    'Question': "What is my average earning each week in this month?",
    'SQLQuery': """SELECT WEEK(Value_date) AS Week, AVG(Deposit_amount) AS Average_Earning 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   AND MONTH(Value_date) = MONTH(CURRENT_DATE()) 
                   GROUP BY WEEK(Value_date)"""
},
{
    'Question': "What were my earnings each week in the previous month?",
    'SQLQuery': """SELECT WEEK(Value_date) AS Week, SUM(Deposit_amount) AS Total_Earnings 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   AND MONTH(Value_date) = MONTH(CURRENT_DATE()) - 1
                   GROUP BY WEEK(Value_date)"""
},
    {
    'Question': "What was my net worth previous year?",
    'SQLQuery': """SELECT (SUM(Deposit_amount) - SUM(Withdrawal_amount)) AS Net_Worth
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) - 1"""
},
{
    'Question': "What is my net worth this year?",
    'SQLQuery': """SELECT (SUM(Deposit_amount) - SUM(Withdrawal_amount)) AS Net_Worth
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "What was my bank balance in year 2021?",
    'SQLQuery': """SELECT Balance_amount 
                   FROM transactions 
                   WHERE YEAR(Value_date) = 2021 
                   ORDER BY Value_date DESC 
                   LIMIT 1"""
},
{
    'Question': "How much money did I spend this year?",
    'SQLQuery': """SELECT SUM(Withdrawal_amount) AS Total_Spending 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "How much money did I spend till now?",
    'SQLQuery': """SELECT SUM(Withdrawal_amount) AS Total_Spending 
                   FROM transactions"""
},
{
    'Question': "How much money did I spend this week?",
    'SQLQuery': """SELECT SUM(Withdrawal_amount) AS Total_Spending 
                   FROM transactions 
                   WHERE YEARWEEK(Value_date, 1) = YEARWEEK(CURRENT_DATE(), 1)"""
},
{
    'Question': "How much money did I spend previous week?",
    'SQLQuery': """SELECT SUM(Withdrawal_amount) AS Total_Spending 
                   FROM transactions 
                   WHERE YEARWEEK(Value_date, 1) = YEARWEEK(CURRENT_DATE(), 1) - 1"""
},
{
    'Question': "How much money did I spend this month?",
    'SQLQuery': """SELECT SUM(Withdrawal_amount) AS Total_Spending 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   AND MONTH(Value_date) = MONTH(CURRENT_DATE())"""
},
{
    'Question': "How much money did I spend last month?",
    'SQLQuery': """SELECT SUM(Withdrawal_amount) AS Total_Spending 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   AND MONTH(Value_date) = MONTH(CURRENT_DATE()) - 1"""
},
    {
    'Question': "What is my highest spending month this year?",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, SUM(Withdrawal_amount) AS Total_Spending 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY MONTH(Value_date) 
                   ORDER BY Total_Spending DESC 
                   LIMIT 1"""
},
{
    'Question': "What is my highest earning month this year?",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, SUM(Deposit_amount) AS Total_Earnings 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY MONTH(Value_date) 
                   ORDER BY Total_Earnings DESC 
                   LIMIT 1"""
},
{
    'Question': "What is my lowest spending month this year?",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, SUM(Withdrawal_amount) AS Total_Spending 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY MONTH(Value_date) 
                   ORDER BY Total_Spending ASC 
                   LIMIT 1"""
},
{
    'Question': "What is my lowest earning month this year?",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, SUM(Deposit_amount) AS Total_Earnings 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY MONTH(Value_date) 
                   ORDER BY Total_Earnings ASC 
                   LIMIT 1"""
},
{
    'Question': "What is my average monthly income this year?",
    'SQLQuery': """SELECT AVG(Total_Earnings) AS Average_Income 
                   FROM (
                       SELECT SUM(Deposit_amount) AS Total_Earnings 
                       FROM transactions 
                       WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                       GROUP BY MONTH(Value_date)
                   ) AS MonthlyEarnings"""
},
{
    'Question': "What is my average monthly spending this year?",
    'SQLQuery': """SELECT AVG(Total_Spending) AS Average_Spending 
                   FROM (
                       SELECT SUM(Withdrawal_amount) AS Total_Spending 
                       FROM transactions 
                       WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                       GROUP BY MONTH(Value_date)
                   ) AS MonthlySpending"""
},
{
    'Question': "What is my largest transaction this year?",
    'SQLQuery': """SELECT * 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   ORDER BY GREATEST(Withdrawal_amount, Deposit_amount) DESC 
                   LIMIT 1"""
},
{
    'Question': "What is my smallest transaction this year?",
    'SQLQuery': """SELECT * 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   ORDER BY LEAST(Withdrawal_amount, Deposit_amount) ASC 
                   LIMIT 1"""
},
{
    'Question': "How many deposits did I make this year?",
    'SQLQuery': """SELECT COUNT(*) AS Total_Deposits 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   AND Deposit_amount IS NOT NULL"""
},
{
    'Question': "How many withdrawals did I make this year?",
    'SQLQuery': """SELECT COUNT(*) AS Total_Withdrawals 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   AND Withdrawal_amount IS NOT NULL"""
},
{
    'Question': "What is my total balance at the end of each year?",
    'SQLQuery': """SELECT YEAR(Value_date) AS Year, Balance_amount 
                   FROM transactions 
                   WHERE Value_date IN (
                       SELECT MAX(Value_date) 
                       FROM transactions 
                       GROUP BY YEAR(Value_date)
                   ) 
                   GROUP BY YEAR(Value_date)"""
},
{
    'Question': "What is my highest balance this year?",
    'SQLQuery': """SELECT MAX(Balance_amount) AS Highest_Balance 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "What is my lowest balance this year?",
    'SQLQuery': """SELECT MIN(Balance_amount) AS Lowest_Balance 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "How many transactions were above $1000 this year?",
    'SQLQuery': """SELECT COUNT(*) AS High_Value_Transactions 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   AND (Withdrawal_amount > 1000 OR Deposit_amount > 1000)"""
},
{
    'Question': "How many transactions were below $100 this year?",
    'SQLQuery': """SELECT COUNT(*) AS Low_Value_Transactions 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   AND (Withdrawal_amount < 100 OR Deposit_amount < 100)"""
},
{
    'Question': "What is the average balance in my account this year?",
    'SQLQuery': """SELECT AVG(Balance_amount) AS Average_Balance 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "How many days did I have a balance below $500 this year?",
    'SQLQuery': """SELECT COUNT(DISTINCT Value_date) AS Days_Below_500 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   AND Balance_amount < 500"""
},
{
    'Question': "How many days did I have a balance above $5000 this year?",
    'SQLQuery': """SELECT COUNT(DISTINCT Value_date) AS Days_Above_5000 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   AND Balance_amount > 5000"""
},
{
    'Question': "How much did I spend on the highest spending day this year?",
    'SQLQuery': """SELECT MAX(Total_Spending) AS Highest_Spending_Day 
                   FROM (
                       SELECT SUM(Withdrawal_amount) AS Total_Spending 
                       FROM transactions 
                       WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                       GROUP BY DATE(Value_date)
                   ) AS DailySpending"""
},
{
    'Question': "How much did I earn on the highest earning day this year?",
    'SQLQuery': """SELECT MAX(Total_Earnings) AS Highest_Earning_Day 
                   FROM (
                       SELECT SUM(Deposit_amount) AS Total_Earnings 
                       FROM transactions 
                       WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                       GROUP BY DATE(Value_date)
                   ) AS DailyEarnings"""
},
    {
    'Question': "What is my total income from last year?",
    'SQLQuery': """SELECT SUM(Deposit_amount) AS Total_Income 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) - 1"""
},
{
    'Question': "What is my total spending from last year?",
    'SQLQuery': """SELECT SUM(Withdrawal_amount) AS Total_Spending 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) - 1"""
},
{
    'Question': "What is the average daily spending in the last month?",
    'SQLQuery': """SELECT AVG(Daily_Spending) AS Average_Daily_Spending 
                   FROM (
                       SELECT DATE(Value_date) AS Date, SUM(Withdrawal_amount) AS Daily_Spending 
                       FROM transactions 
                       WHERE Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH) 
                       GROUP BY DATE(Value_date)
                   ) AS DailySpending"""
},
{
    'Question': "What is the average daily income in the last month?",
    'SQLQuery': """SELECT AVG(Daily_Income) AS Average_Daily_Income 
                   FROM (
                       SELECT DATE(Value_date) AS Date, SUM(Deposit_amount) AS Daily_Income 
                       FROM transactions 
                       WHERE Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH) 
                       GROUP BY DATE(Value_date)
                   ) AS DailyIncome"""
},
{
    'Question': "What is my largest withdrawal amount this year?",
    'SQLQuery': """SELECT MAX(Withdrawal_amount) AS Largest_Withdrawal 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "What is my largest deposit amount this year?",
    'SQLQuery': """SELECT MAX(Deposit_amount) AS Largest_Deposit 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "How much did I save in total last year?",
    'SQLQuery': """SELECT SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Total_Savings 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) - 1"""
},
{
    'Question': "How much did I save in total this year?",
    'SQLQuery': """SELECT SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Total_Savings 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "How much did I save each month this year?",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Monthly_Savings 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY MONTH(Value_date)"""
},
{
    'Question': "What is the average monthly savings this year?",
    'SQLQuery': """SELECT AVG(Monthly_Savings) AS Average_Monthly_Savings 
                   FROM (
                       SELECT MONTH(Value_date) AS Month, SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Monthly_Savings 
                       FROM transactions 
                       WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                       GROUP BY MONTH(Value_date)
                   ) AS MonthlySavings"""
},
{
    'Question': "What is my net income this year?",
    'SQLQuery': """SELECT SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Net_Income 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "What is my net income last year?",
    'SQLQuery': """SELECT SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Net_Income 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) - 1"""
},
{
    'Question': "What is the total number of deposits this year?",
    'SQLQuery': """SELECT COUNT(*) AS Total_Deposits 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) AND Deposit_amount IS NOT NULL"""
},
{
    'Question': "What is the total number of withdrawals this year?",
    'SQLQuery': """SELECT COUNT(*) AS Total_Withdrawals 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) AND Withdrawal_amount IS NOT NULL"""
},
{
    'Question': "What is the highest balance in my account this year?",
    'SQLQuery': """SELECT MAX(Balance_amount) AS Highest_Balance 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "What is the lowest balance in my account this year?",
    'SQLQuery': """SELECT MIN(Balance_amount) AS Lowest_Balance 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "How much did I earn each quarter this year?",
    'SQLQuery': """SELECT QUARTER(Value_date) AS Quarter, SUM(Deposit_amount) AS Total_Earnings 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY QUARTER(Value_date)"""
},
{
    'Question': "How much did I spend each quarter this year?",
    'SQLQuery': """SELECT QUARTER(Value_date) AS Quarter, SUM(Withdrawal_amount) AS Total_Spending 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY QUARTER(Value_date)"""
},
{
    'Question': "How much did I save each quarter this year?",
    'SQLQuery': """SELECT QUARTER(Value_date) AS Quarter, SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Total_Savings 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY QUARTER(Value_date)"""
},
{
    'Question': "How much did I earn each day this week?",
    'SQLQuery': """SELECT DATE(Value_date) AS Date, SUM(Deposit_amount) AS Total_Earnings 
                   FROM transactions 
                   WHERE Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 WEEK) 
                   GROUP BY DATE(Value_date)"""
}
    ,
    {
    'Question': "What is my average income each month in the current year?",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, AVG(Deposit_amount) AS Average_Income 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY MONTH(Value_date)"""
},
{
    'Question': "What is my total number of transactions each month this year?",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, COUNT(*) AS Total_Transactions 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY MONTH(Value_date)"""
},
{
    'Question': "What is my average balance each month this year?",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, AVG(Balance_amount) AS Average_Balance 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY MONTH(Value_date)"""
},
{
    'Question': "What is my highest deposit each month this year?",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, MAX(Deposit_amount) AS Highest_Deposit 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY MONTH(Value_date)"""
},
{
    'Question': "What is my highest withdrawal each month this year?",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, MAX(Withdrawal_amount) AS Highest_Withdrawal 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY MONTH(Value_date)"""
},
{
    'Question': "How many transactions did I make each quarter this year?",
    'SQLQuery': """SELECT QUARTER(Value_date) AS Quarter, COUNT(*) AS Total_Transactions 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY QUARTER(Value_date)"""
},
{
    'Question': "What is my total income each quarter this year?",
    'SQLQuery': """SELECT QUARTER(Value_date) AS Quarter, SUM(Deposit_amount) AS Total_Income 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY QUARTER(Value_date)"""
},
{
    'Question': "What is my total spending each quarter this year?",
    'SQLQuery': """SELECT QUARTER(Value_date) AS Quarter, SUM(Withdrawal_amount) AS Total_Spending 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY QUARTER(Value_date)"""
},
{
    'Question': "What is my average balance each quarter this year?",
    'SQLQuery': """SELECT QUARTER(Value_date) AS Quarter, AVG(Balance_amount) AS Average_Balance 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY QUARTER(Value_date)"""
},
{
    'Question': "How much did I save each quarter in the last year?",
    'SQLQuery': """SELECT QUARTER(Value_date) AS Quarter, SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Total_Savings 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) - 1 
                   GROUP BY QUARTER(Value_date)"""
},
{
    'Question': "What is my total income this quarter?",
    'SQLQuery': """SELECT SUM(Deposit_amount) AS Total_Income 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) AND QUARTER(Value_date) = QUARTER(CURRENT_DATE())"""
},
{
    'Question': "What is my total spending this quarter?",
    'SQLQuery': """SELECT SUM(Withdrawal_amount) AS Total_Spending 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) AND QUARTER(Value_date) = QUARTER(CURRENT_DATE())"""
},
{
    'Question': "What is my total income last quarter?",
    'SQLQuery': """SELECT SUM(Deposit_amount) AS Total_Income 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) AND QUARTER(Value_date) = QUARTER(CURRENT_DATE()) - 1"""
},
{
    'Question': "What is my total spending last quarter?",
    'SQLQuery': """SELECT SUM(Withdrawal_amount) AS Total_Spending 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) AND QUARTER(Value_date) = QUARTER(CURRENT_DATE()) - 1"""
},
{
    'Question': "How much did I save last quarter?",
    'SQLQuery': """SELECT SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Total_Savings 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) AND QUARTER(Value_date) = QUARTER(CURRENT_DATE()) - 1"""
},
{
    'Question': "What is my highest balance in the last quarter?",
    'SQLQuery': """SELECT MAX(Balance_amount) AS Highest_Balance 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) AND QUARTER(Value_date) = QUARTER(CURRENT_DATE()) - 1"""
},
{
    'Question': "How much did I earn each day in the last 30 days?",
    'SQLQuery': """SELECT DATE(Value_date) AS Date, SUM(Deposit_amount) AS Daily_Earnings 
                   FROM transactions 
                   WHERE Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY) 
                   GROUP BY DATE(Value_date)"""
},
{
    'Question': "How much did I spend each day in the last 30 days?",
    'SQLQuery': """SELECT DATE(Value_date) AS Date, SUM(Withdrawal_amount) AS Daily_Spending 
                   FROM transactions 
                   WHERE Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY) 
                   GROUP BY DATE(Value_date)"""
},
{
    'Question': "What is my average income each day in the last 30 days?",
    'SQLQuery': """SELECT AVG(Daily_Earnings) AS Average_Daily_Income 
                   FROM (
                       SELECT DATE(Value_date) AS Date, SUM(Deposit_amount) AS Daily_Earnings 
                       FROM transactions 
                       WHERE Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY) 
                       GROUP BY DATE(Value_date)
                   ) AS DailyIncome"""
},
{
    'Question': "What is my average spending each day in the last 30 days?",
    'SQLQuery': """SELECT AVG(Daily_Spending) AS Average_Daily_Spending 
                   FROM (
                       SELECT DATE(Value_date) AS Date, SUM(Withdrawal_amount) AS Daily_Spending 
                       FROM transactions 
                       WHERE Value_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY) 
                       GROUP BY DATE(Value_date)
                   ) AS DailySpending"""
}
    ,
    {
    'Question': "What is my highest balance ever recorded?",
    'SQLQuery': """SELECT MAX(Balance_amount) AS Highest_Balance 
                   FROM transactions"""
},
{
    'Question': "What is my lowest balance ever recorded?",
    'SQLQuery': """SELECT MIN(Balance_amount) AS Lowest_Balance 
                   FROM transactions"""
},
{
    'Question': "What is the total number of transactions this year?",
    'SQLQuery': """SELECT COUNT(*) AS Total_Transactions 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "How much did I earn each week this month?",
    'SQLQuery': """SELECT WEEK(Value_date) AS Week, SUM(Deposit_amount) AS Weekly_Earnings 
                   FROM transactions 
                   WHERE MONTH(Value_date) = MONTH(CURRENT_DATE()) AND YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY WEEK(Value_date)"""
},
{
    'Question': "How much did I spend each week this month?",
    'SQLQuery': """SELECT WEEK(Value_date) AS Week, SUM(Withdrawal_amount) AS Weekly_Spending 
                   FROM transactions 
                   WHERE MONTH(Value_date) = MONTH(CURRENT_DATE()) AND YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY WEEK(Value_date)"""
},
{
    'Question': "What is the total number of deposits made this year?",
    'SQLQuery': """SELECT COUNT(*) AS Total_Deposits 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) AND Deposit_amount > 0"""
},
{
    'Question': "What is the total number of withdrawals made this year?",
    'SQLQuery': """SELECT COUNT(*) AS Total_Withdrawals 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) AND Withdrawal_amount > 0"""
},
{
    'Question': "What is my total balance at the end of each quarter this year?",
    'SQLQuery': """SELECT YEAR(Value_date) AS Year, QUARTER(Value_date) AS Quarter, Balance_amount 
                   FROM transactions 
                   WHERE Value_date IN (
                       SELECT MAX(Value_date) 
                       FROM transactions 
                       WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                       GROUP BY YEAR(Value_date), QUARTER(Value_date)
                   ) 
                   GROUP BY YEAR(Value_date), QUARTER(Value_date)"""
},
{
    'Question': "How much did I save each month this year?",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Monthly_Savings 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY MONTH(Value_date)"""
},
{
    'Question': "How much did I earn each quarter in the previous year?",
    'SQLQuery': """SELECT QUARTER(Value_date) AS Quarter, SUM(Deposit_amount) AS Quarterly_Earnings 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) - 1 
                   GROUP BY QUARTER(Value_date)"""
},
{
    'Question': "How much did I spend each quarter in the previous year?",
    'SQLQuery': """SELECT QUARTER(Value_date) AS Quarter, SUM(Withdrawal_amount) AS Quarterly_Spending 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) - 1 
                   GROUP BY QUARTER(Value_date)"""
},
{
    'Question': "What is the average amount per transaction this year?",
    'SQLQuery': """SELECT AVG(Withdrawal_amount + Deposit_amount) AS Average_Transaction_Amount 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "What is the highest deposit made this year?",
    'SQLQuery': """SELECT MAX(Deposit_amount) AS Highest_Deposit 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "What is the highest withdrawal made this year?",
    'SQLQuery': """SELECT MAX(Withdrawal_amount) AS Highest_Withdrawal 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "How much did I save last year?",
    'SQLQuery': """SELECT SUM(Deposit_amount) - SUM(Withdrawal_amount) AS Total_Savings 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) - 1"""
},
{
    'Question': "How much did I earn each day this week?",
    'SQLQuery': """SELECT DATE(Value_date) AS Date, SUM(Deposit_amount) AS Daily_Earnings 
                   FROM transactions 
                   WHERE YEARWEEK(Value_date, 1) = YEARWEEK(CURRENT_DATE(), 1) 
                   GROUP BY DATE(Value_date)"""
},
{
    'Question': "How much did I spend each day this week?",
    'SQLQuery': """SELECT DATE(Value_date) AS Date, SUM(Withdrawal_amount) AS Daily_Spending 
                   FROM transactions 
                   WHERE YEARWEEK(Value_date, 1) = YEARWEEK(CURRENT_DATE(), 1) 
                   GROUP BY DATE(Value_date)"""
},
{
    'Question': "What is my average daily balance this month?",
    'SQLQuery': """SELECT AVG(Balance_amount) AS Average_Daily_Balance 
                   FROM transactions 
                   WHERE MONTH(Value_date) = MONTH(CURRENT_DATE()) AND YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "How many transactions did I make each day this month?",
    'SQLQuery': """SELECT DATE(Value_date) AS Date, COUNT(*) AS Total_Transactions 
                   FROM transactions 
                   WHERE MONTH(Value_date) = MONTH(CURRENT_DATE()) AND YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY DATE(Value_date)"""
},
{
    'Question': "What is the average amount per transaction this month?",
    'SQLQuery': """SELECT AVG(Withdrawal_amount + Deposit_amount) AS Average_Transaction_Amount 
                   FROM transactions 
                   WHERE MONTH(Value_date) = MONTH(CURRENT_DATE()) AND YEAR(Value_date) = YEAR(CURRENT_DATE())"""
}
,
    

{
    'Question': "What is the total number of transactions made last year?",
    'SQLQuery': """SELECT COUNT(*) AS Total_Transactions 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) - 1"""
},
{
    'Question': "What is the total number of transactions made each month last year?",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, COUNT(*) AS Total_Transactions 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) - 1 
                   GROUP BY MONTH(Value_date)"""
},
{
    'Question': "How much did I earn each week last month?",
    'SQLQuery': """SELECT WEEK(Value_date) AS Week, SUM(Deposit_amount) AS Weekly_Earnings 
                   FROM transactions 
                   WHERE MONTH(Value_date) = MONTH(DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH)) AND YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY WEEK(Value_date)"""
},
{
    'Question': "How much did I spend each week last month?",
    'SQLQuery': """SELECT WEEK(Value_date) AS Week, SUM(Withdrawal_amount) AS Weekly_Spending 
                   FROM transactions 
                   WHERE MONTH(Value_date) = MONTH(DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH)) AND YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY WEEK(Value_date)"""
},
{
    'Question': "What is my highest spending in a single transaction this year?",
    'SQLQuery': """SELECT MAX(Withdrawal_amount) AS Highest_Spending 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "What is my highest earning in a single transaction this year?",
    'SQLQuery': """SELECT MAX(Deposit_amount) AS Highest_Earning 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "What is my lowest spending in a single transaction this year?",
    'SQLQuery': """SELECT MIN(Withdrawal_amount) AS Lowest_Spending 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "What is my lowest earning in a single transaction this year?",
    'SQLQuery': """SELECT MIN(Deposit_amount) AS Lowest_Earning 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE())"""
},
{
    'Question': "What is my average balance each month this year?",
    'SQLQuery': """SELECT MONTH(Value_date) AS Month, AVG(Balance_amount) AS Average_Balance 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY MONTH(Value_date)"""
},
{
    'Question': "What is my total earnings for each day this month?",
    'SQLQuery': """SELECT DATE(Value_date) AS Date, SUM(Deposit_amount) AS Total_Earnings 
                   FROM transactions 
                   WHERE MONTH(Value_date) = MONTH(CURRENT_DATE()) AND YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY DATE(Value_date)"""
},
{
    'Question': "What is my total spendings for each day last month?",
    'SQLQuery': """SELECT DATE(Value_date) AS Date, SUM(Withdrawal_amount) AS Total_Spendings 
                   FROM transactions 
                   WHERE MONTH(Value_date) = MONTH(DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH)) AND YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY DATE(Value_date)"""
},
{
    'Question': "What is my highest balance at the end of each month last year?",
    'SQLQuery': """SELECT YEAR(Value_date) AS Year, MONTH(Value_date) AS Month, MAX(Balance_amount) AS Highest_Balance 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) - 1 
                   GROUP BY YEAR(Value_date), MONTH(Value_date)"""
},
{
    'Question': "What is my lowest balance at the end of each month last year?",
    'SQLQuery': """SELECT YEAR(Value_date) AS Year, MONTH(Value_date) AS Month, MIN(Balance_amount) AS Lowest_Balance 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) - 1 
                   GROUP BY YEAR(Value_date), MONTH(Value_date)"""
},
{
    'Question': "What is the total number of transactions made each week this month?",
    'SQLQuery': """SELECT WEEK(Value_date) AS Week, COUNT(*) AS Total_Transactions 
                   FROM transactions 
                   WHERE MONTH(Value_date) = MONTH(CURRENT_DATE()) AND YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY WEEK(Value_date)"""
},
{
    'Question': "What is my total earnings for each week this year?",
    'SQLQuery': """SELECT WEEK(Value_date) AS Week, SUM(Deposit_amount) AS Weekly_Earnings 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY WEEK(Value_date)"""
},
{
    'Question': "What is my total spendings for each week this year?",
    'SQLQuery': """SELECT WEEK(Value_date) AS Week, SUM(Withdrawal_amount) AS Weekly_Spendings 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY WEEK(Value_date)"""
},
{
    'Question': "How many transactions did I make each day this week?",
    'SQLQuery': """SELECT DATE(Value_date) AS Date, COUNT(*) AS Total_Transactions 
                   FROM transactions 
                   WHERE YEARWEEK(Value_date, 1) = YEARWEEK(CURRENT_DATE(), 1) 
                   GROUP BY DATE(Value_date)"""
},
{
    'Question': "How many transactions did I make each day last week?",
    'SQLQuery': """SELECT DATE(Value_date) AS Date, COUNT(*) AS Total_Transactions 
                   FROM transactions 
                   WHERE YEARWEEK(Value_date, 1) = YEARWEEK(DATE_SUB(CURRENT_DATE(), INTERVAL 1 WEEK), 1) 
                   GROUP BY DATE(Value_date)"""
},
{
    'Question': "What is my average balance each week this year?",
    'SQLQuery': """SELECT WEEK(Value_date) AS Week, AVG(Balance_amount) AS Average_Balance 
                   FROM transactions 
                   WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) 
                   GROUP BY WEEK(Value_date)"""
},
{
    'Question': "What is my total balance at the end of each quarter last year?",
    'SQLQuery': """SELECT YEAR(Value_date) AS Year, QUARTER(Value_date) AS Quarter, Balance_amount 
                   FROM transactions 
                   WHERE Value_date IN (
                       SELECT MAX(Value_date) 
                       FROM transactions 
                       WHERE YEAR(Value_date) = YEAR(CURRENT_DATE()) - 1 
                       GROUP BY YEAR(Value_date), QUARTER(Value_date)
                   ) 
                   GROUP BY YEAR(Value_date), QUARTER(Value_date)"""
}


]

