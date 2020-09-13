# import modules
import os
import csv
import pandas as pd

# Make data file into variable
# filepath = 'Resources/budget_data.csv'
budget_data = os.path.join('Resources', 'budget_data.csv')

total = 0
months = 0

with open(budget_data, "r") as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=",")
    headers = next(budget_file)

    for rows in budget_reader:
        total = int(rows[1]) + total
    


       


print("Financial Analysis")
print("--------------------------")
print(f"Total Months:  {months}")
print(f"Total: {total}")
print("Average Change: ")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")

