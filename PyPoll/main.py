# First we'll import the os moduel and module for reading CSV files

import os
import csv
# Path to collect data from the Resources folder

csvpath = os.path.join("Resources","election_data.csv")
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"Header:{csv_header}")

    total=0
    candidatelist = []
    unique_candidate = []
    vote=[]
    vote_percent=[]

    for rows in csvreader:
        total = total + 1
        candidatelist.append(rows[2])
        
    for x in set(candidatelist):
        unique_candidate.append(x)
        y = candidatelist.count(x)
        vote.append(y)
        p_count = round((y/total)*100,2)
        vote_percent.append(p_count)
    
    win_vote = max(vote)
    winner = unique_candidate[vote.index(win_vote)]
    print("-------------------------")
    print("Election Results")   
    print("-------------------------")
    print("Total Votes :" + str(total))    
    print("-------------------------")
    for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote[i])+ ")")
    print("-------------------------")
    print("The winner is: " + winner)
    print("-------------------------")


    f = open("analysis/Election Result.txt", "w")
    f.write("\n-------------------------")
    f.write("\nElection Results")   
    f.write("\n-------------------------")
    f.write("\nTotal Votes :" + str(total))    
    f.write("\n-------------------------")
    for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote[i])+ ")")
    f.write("\n-------------------------")
    f.write("\nThe winner is: " + winner)
    f.write("\n-------------------------")