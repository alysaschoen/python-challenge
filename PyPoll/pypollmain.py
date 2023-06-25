import os
import csv

data_csv= os.path.join("/Users/alysaschoenfelder/Documents/GitHub/python-challenge/Starter_Code/PyPoll/Resources/election_data.csv")

candidate_dictionary = {}
vote_total= 0

with open (data_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next (csvreader)

    for row in csvreader:
        vote_total += 1
        if row[2] not in candidate_dictionary:
            candidate_dictionary[row[2]] = 1
        else:
            candidate_dictionary[row[2]] += 1

print (f' Election Results')
print (f' =================================== ')
print (f' Total Votes : {vote_total}' )
print (f' =================================== ')

for candidate, votes in candidate_dictionary.items():
  print(candidate + ": " + "{:.3%}".format(votes/vote_total) + "   (" +  str(votes) + ")")

print (f' =================================== ')

winning_candidate = max(candidate_dictionary, key=candidate_dictionary.get)

print (f' Winner: {winning_candidate}')

print (f' =================================== ')


candidate_output = os.path.join("/Users/alysaschoenfelder/Documents/GitHub/python-challenge/PyPoll/Analysis", "candidate_analysis.txt")

with open(candidate_output, 'w') as txt_file:
    txt_file.write("===================================")
    txt_file.write("\nElection Results")
    txt_file.write("\n===================================")
    txt_file.write("\nTotal Votes:" + str(vote_total))
    txt_file.write("\n===================================")
    txt_file.write('\n')

    for candidate, votes in candidate_dictionary.items():
        txt_file.write(candidate + ": " + "{:.3%}".format(votes/vote_total) + "   (" +  str(votes) + ")")
        txt_file.write('\n')

    txt_file.write("===================================")
    txt_file.write('\n')
    txt_file.write(f'Winner: {winning_candidate} ')
    txt_file.write('\n')


    
