# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

months = []
revenue = []
monthlychange = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    csv_header = next(csvreader)
    #  print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))
    for i in range(1, len(revenue)):
        monthlychange.append(revenue[i] - revenue[i-1])

totalmonths = len(months)
totalrevenue = sum(revenue)
totalmonthlychange = sum(monthlychange)
averagechange = totalmonthlychange / (totalmonths-1)
formatted = "{:.2f}".format(averagechange)
formattedavg = float(formatted)
greatestincrease = max(monthlychange)
greatestdecrease = min(monthlychange)
girow = monthlychange.index(greatestincrease)
gimonth = months[girow+1]
gdrow = monthlychange.index(greatestdecrease)
gdmonth = months[gdrow+1]

print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total months: {len(months)}')
print(f'Total: ${sum(revenue)}')
print(f'Average Change: ${formattedavg}')
print(f'Greatest Increase in Profits: {gimonth} (${greatestincrease})')
print(f'Greatest Decrease in Profits: {gdmonth} (${greatestdecrease})')