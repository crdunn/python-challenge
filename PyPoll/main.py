import csv
import os

loadFile = os.path.join("Resources", "election_data.csv")

totalVotes = 0

voteDict = {}

with open(loadFile) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:
        totalVotes += 1
        
        if (row[2] not in voteDict):
            voteDict[row[2]] = 1
        else:
            voteDict[row[2]] += 1

print(f"Total Votes: {totalVotes}")
print("-------------------------")
greatest = 0
for key in voteDict:

    print(f"Candidate: {key}")
    print(f"Votes: {voteDict[key]}")
    print(f"Vote %: {round((voteDict[key]/totalVotes)* 100)}%")
    print("-------------------------")
    if (voteDict[key] > greatest):
        greatest = voteDict[key]
        winner = key

print(f"Winner: {winner}")