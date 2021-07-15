
import os

import csv

csvpath = os.path.join(r'C:\Users\joeru\Documents\GitHub\python-challenge\PyBank\Resources\budget_data.csv')

Month = []
Amount = []
MonthChange = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
   # print(f"CSV Header: {csv_header}")
    
    MonthPLChange = 0
    LastMonthAmount = int(0)

    # Read each row of data after the header
    for row in csvreader:

        # Add month
        Month.append(row[0])

        # Add amount
        Amount.append(row[1])
        if LastMonthAmount == 0: LastMonthAmount=int(row[1])
        
        MonthPLChange = int(row[1])-(LastMonthAmount)

        MonthChange.append(int(MonthPLChange))

Mths=(len(Month))
MXMC=(max(MonthChange)) 
MNMC=(min(MonthChange))
SMC=(sum(MonthChange))
AVECH=(sum(MonthChange)/len(MonthChange))


print("Financial Analysis") 
print("_______________________________________________")
print("Total Months:" + str(Mths))
print("Average Change: " + str(AVECH))
print("Greatest Increase in Profits" + str(MXMC))
print("Greatest Decrease in Profits" + str(MNMC))

output_path = os.path.join(r'C:\Users\joeru\Documents\GitHub\python-challenge\PyBank\Resources\Analysis.csv')

with open(output_path, 'w', newline='') as csvfile:
    writer=csv.writer(csvfile)

    writer.writerow("Financial Analysis")
    writer.writerow("_______________________________________________")
    writer.writerow("Total Months:  " + str(Mths))
    writer.writerow("Average Change:  " + str(AVECH))
    writer.writerow("Greatest Increase in Profits  " + str(MXMC))
    writer.writerow("Greatest Decrease in Profits  " + str(MNMC))