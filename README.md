# About

Crypto-FIFO is a program to easily calculate your Crypto inventory cost basis. Accounting for Cryptocurrencies can be challenging; and the need for FIFO cost basis calculation can be costly with subledgers easily costing thousands of dollars per month.
With Crypto-FIFO, simply download your ledger of transactions from Etherscan, clean up the data, run the program, and wait for the magic to happen.
Your output will be an easy-to-read Excel file which you can use for your internal records, to create journal entries, or reconciliation purposes.

# Setup

Users must install the following library:

- Pandas

# Users must set up their excel file as follows
- Have at least 4 columns named exactly: "Date" "Purchases" "Cost" "Sales"
- Date column should be dates
- Purchases column should be the acquisitions of Crypto and must be non-negative
- Cost column should be the spot price of Crypto and must be non-negative
- Sales column should be the amount of Crypto disposed and must be non-negative

Change the variable name DATA_NAME to be the name of your file exactly. E.g. DATA_NAME = "Test Fifo.xlsx"
Change the variable name DATA_OUTPUT to be the desired name of the output file exactly. E.g. DATA_OUTPUT = "Test Fifo Updated.xlsx"

Ensure the Excel file is in the same directory as FIFO.py

# Tools Used

- Pandas
