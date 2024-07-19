# First we'll import the os moduel and module for reading CSV files

import os
import csv
# Path to collect data from the Resources folder

csvpath = os.path.join("Resources","election_data.csv")
# open and read csv
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"Header:{csv_header}")
#set each variables total= total vote candidatelist=list for all candidates unique_candidates=list for different candidates
#vote= vote each candidates get vote percent= percent of each candidates
    total=0
    candidatelist = []
    unique_candidate = []
    vote=[]
    vote_percent=[]
#read through rows get the total votes
    for rows in csvreader:
        total = total + 1
        candidatelist.append(rows[2])
#get a set from the candidatelist to get the unique candidate names       
    for x in set(candidatelist):
        unique_candidate.append(x)
#y is total vote each candidate get       
        y = candidatelist.count(x)
        vote.append(y)
#calculate the percent        
        p_count = round((y/total)*100,2)
        vote_percent.append(p_count)
#find the winner    
    win_vote = max(vote)
    winner = unique_candidate[vote.index(win_vote)]

#print the result
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

#creat the text file with results
    f = open("analysis/Election Result.txt", "w")
    f.write("\n-------------------------")
    f.write("\nElection Results")   
    f.write("\n-------------------------")
    f.write("\nTotal Votes :" + str(total))    
    f.write("\n-------------------------\n")
    for i in range(len(unique_candidate)):
            f.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote[i])+ ")\n")
    f.write("-------------------------")
    f.write("\nThe winner is: " + winner)
    f.write("\n-------------------------")