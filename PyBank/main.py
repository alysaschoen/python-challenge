import os
import csv
#lists
date = []
profit = []
changes = []
#variables
monthly_change= 0
total_change = 0
total_profit = 0
starting_profit = 0
#path for csv
pythonbank_csv = os.path.join("/Users/alysaschoenfelder/Documents/GitHub/python-challenge/Starter_Code/PyBank/Resources/budget_data.csv")
with open (pythonbank_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
# for loop
    for row in csv_reader:
         # assigning data to variables
        date.append(row[0])
        profit.append(float(row[1]))
        # calculating total months, profits, and averages
        months = len(date)
        monthly_profit = int(row[1])
        monthly_change = float(monthly_profit)
        total_change = total_change + monthly_change
        starting_profit = int(row[1])
        changes.append(monthly_change)
        greatest_increase = max(changes)
        increase_date = changes.index(greatest_increase)
        greatest_decrease = min(changes)
        decrease_date = changes.index(greatest_decrease)
        profit_avg = round(total_change/months)
        total_profit = sum(profit)
 



# printing data
print (f"__________________________________________________________")
print (f"Financial Analysis")
print (f"__________________________________________________________")
print (f"\n")
print (f"Total Months: {months}")
print (f"Total Profits: ${total_profit}")
print (f"Average Change: ${profit_avg}")
print (f"Greatest Increase in Profits: {date[increase_date]} --- $ {greatest_increase}")
print (f"Greatest Decrease in Profits: {date[decrease_date]} --- $ {greatest_decrease}")
print ("\n")



#output file 

output_analysis = os.path.join("/Users/alysaschoenfelder/Documents/GitHub/python-challenge/PyBank/Analysis", "financial_analysis.txt")

with open(output_analysis, 'w') as txt_file:
    txt_file.write("__________________________________________________________""\n")
    txt_file.write("\nFinancial Analysis")
    txt_file.write("\n__________________________________________________________")
    txt_file.write("\nTotal Months:" + str(months))
    txt_file.write("\nTotal Profits: " + "$"+str(total_profit))
    txt_file.write("\nAverage Change: " + "$" + str(profit_avg))
    txt_file.write(f"\nGreatest Increase in Profits: {date[increase_date]} --- $ {greatest_increase}")
    txt_file.write(f"\nGreatest Decrease in Profits: {date[decrease_date]} --- $ {greatest_decrease}")



    
        



