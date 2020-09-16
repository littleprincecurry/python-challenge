# import modules
import os
import csv

# Make data file into variable
# filepath = 'Resources/budget_data.csv'
budget_data = os.path.join('Resources', 'budget_data.csv')


months = 0
monthlyProfits = []
# change= 0
# greatest = 0
# gst_month = []
# least = 0
# lst_month = []
# previous_week = 867884

with open(budget_data, "r") as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=",")
    header = next(budget_reader)

    for rows in budget_reader:
        months += 1
        monthlyProfits.append(int(rows[1]))
    



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
print(f"Total Months: {months}")
print(f"Total: ${sum(monthlyProfits)}")
# print(f"Average Change: ${round(avg_change, 2)}")
# print(f"Greatest Increase in Profits: ${gst_month}")
# print(f"Greatest Decrease in Profits: ${lst_month}")

