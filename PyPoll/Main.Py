
import os
import csv

#needed Lists / variables

OutPutLine = []
VotesSubmitted = []
candidate: int 
Winner = "UnDetermined"
WinningVotes = 0  

#Input Source
csvpath = os.path.join(r'C:\Users\joeru\Documents\GitHub\python-challenge\PyPoll\Resources\election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
 
 #  Read votes   
    for row in csvreader:   
        VotesSubmitted.append(row[2])

#Process and aggregate      
candidates = list(set(VotesSubmitted))
VSUBTuple = tuple(VotesSubmitted)
TotalVotesSubmitted = (len(VSUBTuple))      
  
#Build Output List
OutPutLine.append(str(('{:25s}').format('Election Results')))  
OutPutLine.append(str(('{:15s}').format('----------------------------------------')))
OutPutLine.append(str(('{:15s} {:9.0f}').format('Total Votes:           ', TotalVotesSubmitted)))
OutPutLine.append(str(('{:25s}').format('----------------------------------------')))
    
for i in range(len(candidates)):
    candidate = candidates[i]
    CandidateVotes = VSUBTuple.count(candidate)
    if CandidateVotes > WinningVotes:
        WinningVotes = CandidateVotes
        Winner = candidate
    PercentageVote=round((float(CandidateVotes/TotalVotesSubmitted))*100,3)
    OutPutLine.append(str(('{:15s} {:7.2f} {:9.0f}').format(candidate, PercentageVote, CandidateVotes)))

OutPutLine.append(str('{:15s}').format('----------------------------------------'))
OutPutLine.append(str('{:15s} {:10s}').format('Winner:  ', Winner))
OutPutLine.append(str('{:15s}').format('----------------------------------------'))

# Dump Output
OPLLen = len(OutPutLine)
output_path = os.path.join(r'C:\Users\joeru\Documents\GitHub\python-challenge\PyPoll\Resources\Analysis.csv')
with open(output_path, 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter ='\n')
    writer.writerow(((OutPutLine)))

for x in range(0, OPLLen):
    print(str(OutPutLine[x]))