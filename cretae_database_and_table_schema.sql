SELECT * FROM arl1_bank.transactions;

CREATE DATABASE IF NOT EXISTS arl_bank2;


 CREATE TABLE IF NOT EXISTS transactions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Account_No VARCHAR(20) NOT NULL,
        Withdrawal_amount DECIMAL(15, 2) DEFAULT 0,
        Deposit_amount DECIMAL(15, 2) DEFAULT 0,
        Balance_amount DECIMAL(15, 2) DEFAULT 0,
        Value_date DATE NOT NULL,
        Data DATE NOT NULL,
        transaction_details VARCHAR(100) DEFAULT '' 
        );