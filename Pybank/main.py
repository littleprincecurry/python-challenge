import os
import csv

budget_data = os.path.join('Resources/', 'budget_data.csv')

with open(budget_data, "r") as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=",")

    months = len(list(budget_reader)) - 1
    


print("Financial Analysis")
print("--------------------------")
print("Total Months: " + str(months))
print("Total: ")
print("Average Change: ")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")

