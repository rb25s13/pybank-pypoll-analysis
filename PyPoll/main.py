# Create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.


# import modules for data path functions and csv read/writing
import os
import csv

# name the path of the revenue data in the csv file
polldatapath = os.path.join('Resources', 'election_data.csv')

# empty lists to hold data
votes = []
khan = []
correy = []
li = []
otooley = []

# open csv file
with open(polldatapath) as csvfile:

    # csv.reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip the header row
    csv_header = next(csvreader)

    # read the rows after the header
    for row in csvreader:
        # add vote to vote list
        votes.append(row[0])
        # if vote is for Khan, add to list
        if row[2] == 'Khan':
            khan.append(row)
        # if vote is for correy, add to list
        if row[2] == 'Correy':
            correy.append(row)
        # if vote is for Li, add to list
        if row[2] == 'Li':
            li.append(row)
        # if vote is for O'Tooley, add to list
        if row[2] == "O'Tooley":
            otooley.append(row)

# count the total votes and total for each candidate
totalvotes = len(votes)
cktotal = len(khan)
cctotal = len(correy)
cltotal = len(li)
cttotal = len(otooley)

# calculate the percentages using the totals above, format for one decimal place
ckpercent = (cktotal / totalvotes) * 100
formavgck = round(ckpercent, 1)
ccpercent = (cctotal / totalvotes) * 100
formavgcc = round(ccpercent, 1)
clpercent = (cltotal / totalvotes) * 100
formavgcl = round(clpercent, 1)
ctpercent = (cttotal / totalvotes) * 100
formavgct = round(ctpercent, 1)

# list to hold the candidate names
candidatelist = ['Khan', 'Correy', 'Li', "O'Tooley"]
# list to hold the results totals
results = [cktotal, cctotal, cltotal, cttotal]
# the highest total in the results list
mostvotes = max(results)
# position of candidate in the results list
windex = results.index(mostvotes)
# match the windex to the candidate list
winner = candidatelist[windex]

# define the output that needs to print
printoutput = (f'Election Results\n'
                f'----------------------------\n'
                f'Total Votes: {totalvotes}\n'
                f'----------------------------\n'
                f'Khan: {formavgck}% ({cktotal})\n'
                f'Correy: {formavgcc}% ({cctotal})\n'
                f'Li: {formavgcl}% ({cltotal})\n'
                f"O'Tooley: {formavgct}% ({cttotal})\n"
                f'----------------------------\n'
                f'Winner: {winner}\n'
                f'----------------------------\n'
)

# print outout :]
print(printoutput)

# export output to txt file
#
# define output folder name
save_path = 'Analysis'
# join folder path and file path
outputdatapath = os.path.join(save_path, 'Poll_Results.txt')
# open/make the text file named Poll_Results
file = open(outputdatapath, 'w')
# write output to the text file
file.write(f'{printoutput}')
# close the file
file.close()
