# First we'll import the os moduel and module for reading CSV files

import os
import csv
# Path to collect data from the Resources folder

csvpath = os.path.join("Resources","budget_data.csv")
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"Header:{csv_header}")
    
    months=[]
    profit=[]
    changes=[]
    
    for rows in csvreader:
        months.append(rows[0])    
        profit.append(int(rows[1]))

    for x in range(len(profit)-1):
        changes.append((int(profit[x+1])-int(profit[x])))
    
    avergae= round(sum(changes)/len(changes),2)
    total_months=len(months)
    greatest_increase= max(changes)
    greatest_decrease= min(changes)
    greatest_increase_month = changes.index(max(changes)) + 1
    greatest_decrease_month = changes.index(min(changes)) + 1

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:" + str(total_months))
    print("Total:" + "$" + str(sum(profit)))
    print("Average Change:" + "$" + str(avergae))
    print("Greatest Increase in Profits:" + str(months[greatest_increase_month]) + "($ " + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits:" + str(months[greatest_decrease_month]) + "($ " + str(greatest_decrease) + ")")

    f = open("analysis/analysis.txt", "w")
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write("Total Months:" + str(total_months))
    f.write("\nTotal:" + "$" + str(sum(profit)))
    f.write("\nAverage Change:" + "$" + str(avergae))
    f.write("\nGreatest Increase in Profits:" + str(months[greatest_increase_month]) + "($ " + str(greatest_increase) + ")")
    f.write("\nGreatest Decrease in Profits:" + str(months[greatest_decrease_month]) + "($ " + str(greatest_decrease) + ")")
    f.close()