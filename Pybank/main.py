# import modules
import os
import csv

# Make data file into variable
# filepath = 'Resources/budget_data.csv'
budget_data = os.path.join('Resources', 'budget_data.csv')


totalMonths = 0
monthlyProfits = []
monthlyChange = []
# greatest = 0
# gst_month = []
# least = 0
# lst_month = []


with open(budget_data, "r") as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=",")
    header = next(budget_reader)

    for rows in budget_reader:
        totalMonths += 1
        monthlyProfits.append(int(rows[1]))
    
    for months in range(1, len(monthlyProfits)):
        change = monthlyProfits[months] - monthlyProfits[months-1]
        monthlyChange.append(change)

    
averageChange = float(sum(monthlyChange)/len(monthlyChange))
        




#         # greatest / least month calc
#         if greatest < int(rows[1]):
#             greatest = int(rows[1])
#             gst_month = rows
#         if least > int(rows[1]):
#             least = int(rows[1])
#             lst_month = rows

#         # trying desperately to figure out how to get average change
#         change = (int(rows[1]) - previous_week) + change
#         previous_week = int(rows[1])

#         # print(change)
            


        


    
# avg_change = change / 85      


       
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${sum(monthlyProfits)}")
print(f"Average Change: ${round(averageChange, 2)}")
# print(f"Greatest Increase in Profits: ${gst_month}")
# print(f"Greatest Decrease in Profits: ${lst_month}")

