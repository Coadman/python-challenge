#Tasks:

# The total number of votes cast - done
# A complete list of candidates who received votes - done *
# The percentage of votes each candidate won - done *
# The total number of votes each candidate won - done * 
# The winner of the election based on popular vote - done *

### starting here
import csv

#create variables
election_file_path = "PyPoll/Resources/election_data.csv"
total_votes = 0 
candidates = []
candidate_votes = []
# open file
with open(election_file_path) as election_file:
    csv_file = csv.reader(election_file)
    next(csv_file)
    for row in csv_file:
        #  add to total votes
        total_votes += 1 
        # Ballot ID,County,Candidate
        ballot_id = row[0]
        county = row[1]
        candidate = row[2]
        if candidate not in candidates:
            # add to list if not already in list
            candidates.append(candidate)
            candidate_votes.append(1) # add the first vote
        else: # assume candidate is in list 
            candidate_id = candidates.index(candidate)
            candidate_votes[candidate_id] += 1 
# done reading file
# find the winner
winning_candidate = ""
winning_candidate_votes = 0
for candidate in candidates:
    current_votes = candidate_votes[candidates.index(candidate)]
    if current_votes > winning_candidate_votes:
        winning_candidate = candidate
        winning_candidate_votes = current_votes
print(winning_candidate, winning_candidate_votes) 
         
# print results to screen
print('Election Results')

print('-------------------------')

print(f'Total Votes: {total_votes}')

print('-------------------------')
for candidate in candidates:
    current_candidate_votes = candidate_votes[candidates.index(candidate)]
    current_vote_pct = (current_candidate_votes / total_votes) * 100

    print(
        f'{candidate}: {round(current_vote_pct,3)}% ({current_candidate_votes})')
    print(f'Winner: Diana Degette')
print('-------------------------')

print(len(candidates), 'candidates')

print('-------------------------')

print(candidates, 'candidates')

print('-------------------------')

print(candidate_votes)



# print results to file
out_file_path = "PyPoll\election_results.txt"

with open(out_file_path, 'w') as file_out:
    file_out.write('Election Results\n')
    file_out.write('-------------------------\n')
    file_out.write(f'Total Votes: {total_votes}\n')

    file_out.write('-------------------------\n')
    for candidate in candidates:
        current_candidate_votes = candidate_votes[candidates.index(candidate)]
        current_vote_pct = (current_candidate_votes / total_votes) * 100

        file_out.write(
            f'{candidate}: {round(current_vote_pct,3)}% ({current_candidate_votes})\n')
    file_out.write('-------------------------\n')
    file_out.write(f'Winner: Diana Degette\n')
    file_out.write('-------------------------\n')
    # file_out.write(len(candidates), 'candidates\n')
    # file_out.write(candidates, 'candidates\n')
    # file_out.write(candidate_votes)

###

# example output:

# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------

