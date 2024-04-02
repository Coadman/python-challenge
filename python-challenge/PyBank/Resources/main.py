import csv 
filepath = "Starter_Code/PyBank/Resources/budget_data.csv"

row_number = 0

with open(filepath) as text:
    csv_file = csv.reader(text)

    # for row in csv_file:
    #     if row_number
