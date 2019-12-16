import os
import csv

election_csv = os.path.join('Resources', 'election_data.csv')

candidate = []
votes = []
vote_counter = []
percent_list = []

with open(election_csv, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        votes.append(row[1])

        if row[2] in candidate:
            voter_index = candidate.index(row[2])
            vote_counter[voter_index] +=1
        elif row[2] not in candidate:
            candidate.append(row[2])
            vote_counter.append(1)

for candidate_votes in vote_counter:
    percent = (candidate_votes / int(len(votes))) * 100
    percent_list.append(percent)

print("Election Results")
print("----------------")
print(f"Total Votes Cast : {len(votes)}")

for i in range(len(candidate)):
    print(f"{candidate[i]}: {round(percent_list[i],2)}% ({(vote_counter[i])})")
print("----------------")

max_vote = max(vote_counter)
max_vote_index = vote_counter.index(max_vote)
winner = candidate[max_vote_index]

print(f"The Winner Is : {winner}")
print("----------------")

output_file = os.path.join("Resources", "election_analysis.txt")

with open(output_file, "w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("----------------")
    txt_file.write("\n")
    for i in range(len(candidate)):
        txt_file.write(f"{candidate[i]}: {round(percent_list[i],2)}% ({(vote_counter[i])})")
        txt_file.write("\n")
    txt_file.write("----------------")
    txt_file.write("\n")
    txt_file.write(f"The Winner Is : {winner}")
    txt_file.write("\n")
    txt_file.write("----------------")