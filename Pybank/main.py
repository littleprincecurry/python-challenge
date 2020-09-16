# import modules
import os
import csv

# Make data file into variable
# filepath = 'Resources/budget_data.csv'
budget_data = os.path.join('Resources', 'budget_data.csv')


totalMonths = 0
monthlyProfits = []
monthlyChange = []
monthYear = []
greatest = 0
least = 0



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
budgetDict = {monthlyChange[i]: monthYear[i+1] for i in range(len(monthlyChange))}


    
averageChange = float(sum(monthlyChange)/len(monthlyChange))



   
       
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${sum(monthlyProfits)}")
print(f"Average Change: ${round(averageChange, 2)}")
print(f"Greatest Increase in Profits: {budgetDict.get(greatest)} (${greatest})")
print(f"Greatest Decrease in Profits: {budgetDict.get(least)} (${least})")


