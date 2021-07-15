# Create a Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

# import modules for data path functions and csv read/writing
import os
import csv

# name the path of the revenue data in the csv file
revenuedatapath = os.path.join('Resources', 'budget_data.csv')

# empty lists to hold data
months = []
revenue = []
monthlychange = []

# open csv file
with open(revenuedatapath) as csvfile:

    # csv.reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip the header row
    csv_header = next(csvreader)

    # read the rows after the header
    for row in csvreader:
        # add month to months list
        months.append(row[0])
        # add revenue to revenue list
        revenue.append(int(row[1]))
    
    # find the revenue change in the months by subtracting the previous value
    for i in range(1, len(revenue)):
        # add the revenue change value to the monthly change list
        monthlychange.append(revenue[i] - revenue[i-1])

# the total number of months using the len function
totalmonths = len(months)
# the total revenue using the sum function
totalrevenue = sum(revenue)
# the sum of all the monthly change values
totalmonthlychange = sum(monthlychange)
# the average change
averagechange = totalmonthlychange / (totalmonths-1)
# the format for 2 decimal places
formatted = "{:.2f}".format(averagechange)
# the value of average change formatted
formattedavg = float(formatted)
# the greatest increase in monthly change
greatestincrease = max(monthlychange)
# the greatest decrease in monthly change
greatestdecrease = min(monthlychange)
# the index of the greatest increase value
girow = monthlychange.index(greatestincrease)
# the month of the greatest increase value using the index
gimonth = months[girow+1]
# the index of the greatest decrease value
gdrow = monthlychange.index(greatestdecrease)
# the month of the greatest decrease value using the index
gdmonth = months[gdrow+1]

# defining the output
printoutput = (f'Financial Analysis\n'
                f'----------------------------\n'
                f'Total Months: {totalmonths}\n'
                f'Total: ${totalrevenue}\n'
                f'Average Change: ${formattedavg}\n'
                f'Greatest Increase in Profits: {gimonth} (${greatestincrease})\n'
                f'Greatest Decrease in Profits: {gdmonth} (${greatestdecrease})'
            )

# print define out above
print(printoutput)
# define output folder name
save_path = 'Analysis'
# join folder path and file path
outputdatapath = os.path.join(save_path, 'Financial_Analysis.txt')
# open/make the text file named Financial_Analysis
file = open(outputdatapath, 'w')
# write output to the text file
file.write(f'{printoutput}')
# close the file
file.close()