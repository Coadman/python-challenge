# Tasks:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

# Start Here:

import csv

# Create variables
financial_file_path = "python-challenge/PyBank/Resources/budget_data.csv"
total_months = 0
net_total_profit_losses = 0
monthly_changes = []
months = []

# Open file
with open(financial_file_path) as financial_file:
    csv_file = csv.reader(financial_file)
    next(csv_file)  # Skip header
    previous_profit_loss = 0
    for row in csv_file:
        # Count total months
        total_months += 1
        # Calculate net total profit/losses
        net_total_profit_losses += int(row[1])
        # Calculate changes in profit/losses
        if total_months > 1:
            current_profit_loss = int(row[1])
            monthly_change = current_profit_loss - previous_profit_loss
            monthly_changes.append(monthly_change)
            months.append(row[0])
        previous_profit_loss = int(row[1])

# Calculate average change
average_change = sum(monthly_changes) / len(monthly_changes)

# Find greatest increase and decrease in profits
greatest_increase = max(monthly_changes)
greatest_decrease = min(monthly_changes)

# Get corresponding month for greatest increase and decrease
increase_month = months[monthly_changes.index(greatest_increase)]
decrease_month = months[monthly_changes.index(greatest_decrease)]

# Print results to screen
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")

# Print results to file
out_file_path = "Financial_Analysis.txt"
with open(out_file_path, 'w') as file_out:
    file_out.write("Financial Analysis\n")
    file_out.write("-------------------------\n")
    file_out.write(f"Total Months: {total_months}\n")
    file_out.write(f"Total: ${net_total_profit_losses}\n")
    file_out.write(f"Average Change: ${average_change:.2f}\n")
    file_out.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
    file_out.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n")




# expected outcome:

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)
