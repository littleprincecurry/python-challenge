import os
import csv

# 
csv_election = os.path.join("Resources", "election_data.csv")

vote_total = 0
candidateList = []
voteList = []
votes = 0
countList = []


with open(csv_election, "r") as csv_file:
    election_reader = csv.reader(csv_file, delimiter=",")
    header = next(election_reader)

    for rows in election_reader:
        vote_total += 1
        voteList.append(rows[2])
        if rows[2] not in candidateList:
            candidateList.append(rows[2])


for candidate in candidateList:
    for vote in voteList:
        if vote == candidate:
            votes += 1
    countList.append(votes)
    votes = 0 

voteDict = {candidateList[i]: countList[i] for i in range(len(candidateList))} 


winner = max(voteDict, key=voteDict.get)

print('Election Results')
print('-----------------------------------')                
print(f"Total Votes: {vote_total}")
print('-----------------------------------')  
for candidate in candidateList:
    print(f'{candidate}: {round(voteDict.get(candidate) / vote_total * 100, 3)}% ({voteDict.get(candidate)})')
print('-----------------------------------')  
print(f'Winner: {winner}')
print('-----------------------------------')  

file_output = os.path.join('analysis', 'results.txt')
with open(file_output, 'a') as file_writer:
    file_writer.write('Election Results \n')
    file_writer.write('----------------------------------- \n')                
    file_writer.write(f"Total Votes: {vote_total} \n")
    file_writer.write('----------------------------------- \n')  
    for candidate in candidateList:
        file_writer.write(f'{candidate}: {round(voteDict.get(candidate) / vote_total * 100, 3)}% ({voteDict.get(candidate)}) \n')
    file_writer.write('----------------------------------- \n')  
    file_writer.write(f'Winner: {winner}\n')
    file_writer.write('-----------------------------------\n')  
    file_writer.close()