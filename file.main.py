import os
import csv

# Declare file location 
data_output = os.path.join("", "Py_Bank", "budget_data.csv")
print(data_output)

# iterate through rows for the following variables
total_months = []
total_amount = []
average_change = []

with open(r"C:\Users\ramr3_000\Desktop\Python Homework\BH_python-challenge\Py_Bank\budget_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  


# Iterate through the rows 
    for row in csvreader: 

# Append the total months and total amount
        total_months.append(row[0])
        total_amount.append(int(row[1])) 

# How to get monthly change in profits
for i in range(1,len(total_amount)):
    average_change.append(total_amount[i] - (total_amount[i-1])
    
max_increase_value = max(average_change)
min_decrease_value = min(average_change)

max_increase_monthly = average_change.index(max(average_change)) + 1
max_decrease_monthly = average_change.index(min(average_change)) + 1

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_amount)}")
print(f"Average Change: {round(sum(average_change)/len(average_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_monthly]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_monthly]} (${(str(max_decrease_value))})")   