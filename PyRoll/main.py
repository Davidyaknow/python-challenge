f = open("election_data.csv", "r")
f.readline()

num_of_votes = 0
votes = {}
candidate_list = []

for row in f:
    # print(row, end="")
    x = row.split(",")
    x[2] = x[2][:-1]
    # print(x)
    num_of_votes = num_of_votes + 1
    vote_ID = x[0]
    county = x[1]
    candidate = x[2]

    if candidate not in candidate_list:
        candidate_list.append(candidate)
        votes[candidate] = 1
    else:
        votes[candidate] = votes[candidate] + 1


# find the winner
winner = None
winner_vote_count = 0
for candidate in votes:
    if votes[candidate] > winner_vote_count:
        winner = candidate
        winner_vote_count = votes[candidate]


# print(candidate_list)
# print(votes)

def print_result(f_out=None):
    print(f"Election Results",file=f_out)
    print(f"-------------------------",file=f_out)
    print(f"Total Votes: {num_of_votes}",file=f_out)
    print(f"-------------------------",file=f_out)
    for name in candidate_list:
        percentage = round(100 * votes[name] / num_of_votes, 3)
        percentage_str = "%.3f" % percentage
        print(f"{name}: {percentage_str}% ({votes[name]})",file=f_out)
    print(f"-------------------------",file=f_out)
    print(f"Winner: {winner}",file=f_out)
    print(f"-------------------------",file=f_out)

print_result()

f_out = open("election_data_output.txt", "w")
print_result(f_out)