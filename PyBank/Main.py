
import os
import csv

#Input Source
csvpath = os.path.join(r'C:\Users\joeru\Documents\GitHub\python-challenge\PyBank\Resources\budget_data.csv')

# needed Lists
Month = []
Amount = []
MonthChange = []
OutPutLine = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    csv_header = next(csvreader)
    
    MonthPLChange = 0
    LastMonthAmount = int(0)

    # Read each row of data after the header
    for row in csvreader:

        # Add month
        Month.append(row[0])

        # Add amount
        Amount.append(row[1])
        if LastMonthAmount == 0: LastMonthAmount=int(row[1])
        
        #Calc Monthly P/L Change
        MonthPLChange = int(row[1])-(LastMonthAmount)

        #add Monthly Change
        MonthChange.append(int(MonthPLChange))

#Calculations / Agrregations
Mths=(len(Month))
MXMC=(max(MonthChange)) 
MNMC=(min(MonthChange))
SMC=(sum(MonthChange))
AVECH=((sum(MonthChange))/len(MonthChange))

MXMCI=MonthChange.index(MXMC)
MNMCI=MonthChange.index(MNMC)

MXCHM=Month[MXMCI]
MNCHM=Month[MNMCI]

#Build Output List
OutPutLine.append(str("Financial Analysis"))
OutPutLine.append(str("_______________________________________________"))
OutPutLine.append(str("Total Months:" + str(Mths)))
OutPutLine.append(str("Total:" + str(SMC)))
OutPutLine.append(str("Average Change: " + str(round(AVECH,2))))
OutPutLine.append(str("Greatest Increase in Profits " + str(MXCHM)+ " "+ str(MXMC)))
OutPutLine.append(str("Greatest Decrease in Profits " + str(MNCHM)+ " "+ str(MNMC)))
OPLLen = len(OutPutLine)

#Dump output put

output_path = os.path.join(r'C:\Users\joeru\Documents\GitHub\python-challenge\PyBank\Resources\Analysis.csv')
with open(output_path, 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter ='\n')
    writer.writerow(((OutPutLine)))

for x in range(0, OPLLen):
    print(str(OutPutLine[x]))
    