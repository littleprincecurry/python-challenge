# import modules
import os
import csv

# create a pathfile for the data file using the os module 
csv_election = os.path.join("Resources", "election_data.csv")

# create empty variables to store data in
vote_total = 0
candidateList = []
voteList = []
votes = 0
countList = []

# make data file readable with csv module
# count total number of votes and create a list of candidates
with open(csv_election, "r") as csv_file:
    election_reader = csv.reader(csv_file, delimiter=",")
    header = next(election_reader)

    for rows in election_reader:
        vote_total += 1
        voteList.append(rows[2])
        if rows[2] not in candidateList:
            candidateList.append(rows[2])

# tally up votes for each candidate
for candidate in candidateList:
    for vote in voteList:
        if vote == candidate:
            votes += 1
    countList.append(votes)
    votes = 0 

# create a dictionary associating candidates with vote total
voteDict = {candidateList[i]: countList[i] for i in range(len(candidateList))} 

# determine winner using max function on dictionary
winner = max(voteDict, key=voteDict.get)

# print election results to console
print('Election Results')
print('-----------------------------------')                
print(f"Total Votes: {vote_total}")
print('-----------------------------------')  
for candidate in candidateList:
    print(f'{candidate}: {round(voteDict.get(candidate) / vote_total * 100, 3)}% ({voteDict.get(candidate)})')
print('-----------------------------------')  
print(f'Winner: {winner}')
print('-----------------------------------')

# create a text file containing election results
file_output = os.path.join('analysis', 'results.txt')
with open(file_output, 'w') as file_writer:
    file_writer.write(
        'Election Results \n'
        '----------------------------------- \n'                
        f"Total Votes: {vote_total} \n"
        '----------------------------------- \n'
        )  
    for candidate in candidateList:
        file_writer.write(f'{candidate}: {round(voteDict.get(candidate) / vote_total * 100, 3)}% ({voteDict.get(candidate)}) \n')
    file_writer.write(
        '----------------------------------- \n'  
        f'Winner: {winner}\n'
        '-----------------------------------\n'
        )  
    file_writer.close()