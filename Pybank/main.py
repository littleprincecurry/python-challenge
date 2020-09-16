# import modules
import os
import csv

# Make data file into variable
# filepath = 'Resources/budget_data.csv'
budget_data = os.path.join('Resources', 'budget_data.csv')

# make empty variables
totalMonths = 0
monthlyProfits = []
monthlyChange = []
monthYear = []
greatest = 0
least = 0


# open csv file, analyse data using foor loop, store into variables
with open(budget_data, "r") as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=",")
    header = next(budget_reader)

    for rows in budget_reader:
        totalMonths += 1
        monthYear.append(rows[0])
        monthlyProfits.append(int(rows[1]))
         
    for months in range(1, len(monthlyProfits)):
        change = monthlyProfits[months] - monthlyProfits[months-1]
        monthlyChange.append(change)

    for x in monthlyChange:
        if greatest < x:
            greatest = x
        if least > x:
            least = x

# Create a dictionary associating change in value with associated month            
budgetDict = {monthlyChange[i]: monthYear[i+1] for i in range(len(monthlyChange))}


# get the average overall change in value    
averageChange = float(sum(monthlyChange)/len(monthlyChange))

# print results to console      
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${sum(monthlyProfits)}")
print(f"Average Change: ${round(averageChange, 2)}")
print(f"Greatest Increase in Profits: {budgetDict.get(greatest)} (${greatest})")
print(f"Greatest Decrease in Profits: {budgetDict.get(least)} (${least})")

# write results to text file
fileOutput = os.path.join('analysis', 'results.txt')
with open(fileOutput, 'w') as fileWriter:
    fileWriter.write(
        "Financial Analysis\n"
        "--------------------------\n"
        f"Total Months: {totalMonths}\n"
        f"Total: ${sum(monthlyProfits)}\n"
        f"Average Change: ${round(averageChange, 2)}\n"
        f"Greatest Increase in Profits: {budgetDict.get(greatest)} (${greatest})\n"
        f"Greatest Decrease in Profits: {budgetDict.get(least)} (${least})\n"
    )
    fileWriter.close()
