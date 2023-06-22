import os
import csv

#declare variables, lists, and dictionary
vote_total = 0
candidate = []
candidates_list = {}
candidate_vote = {}
winning_candidate = ""
winning_votes = 0

#define path to csv
data_csv = os.path.join("/Users/alysaschoenfelder/Documents/GitHub/python-challenge/Starter_Code/PyPoll/Resources/election_data.csv")
output_file = os.path.join("/Users/alysaschoenfelder/Documents/GitHub/python-challenge/PyPoll/Analysis", "poll_results.text")

# open csv to read
with open (data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next (csvreader)
# read data
    for row in csvreader:
        vote_total = vote_total + 1
        candidate = row[2]
        if candidate not in candidates_list:
            candidates_list.append(candidate)
            candidate_vote[candidate] = 0
            candidate_vote[candidate] = candidate_vote[candidate] + 1
# testing data
print ("Election Results")
print ("_______________________________________")
print ("Total Votes: " + str(vote_total))
print ("_______________________________________")
#
#for candidate in candidate_vote:
   # percent = (candidate_vote[candidate]/vote_total) * 100
# testing results
# print (candidate + ":" + str(percent) + "%" + " (candidate_vote[candidate])")
# need to reformat percentages

for candidate in 
    percent = (candidate_vote[candidate]/vote_total) * 100
    format_percent = ":.3".format(percent)

#print (candidate + ":" + str(format_percent) + "%" + " (candidate_vote[candidate])")