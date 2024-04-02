# Tasks:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

# Start Here:

import csv

#create variables
budget_file_path = "PyPoll/Resources/budget_data.csv"
month_and_yr = []
# open file
with open(budget_file_path) as budget_file:
    csv_file = csv.reader(budget_file)
    next(csv_file)
    for row in csv_file:
        month_and_yr = row[0]
        print(month_and_yr)