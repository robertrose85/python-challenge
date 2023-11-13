import csv, os
from operator import itemgetter

# Open csv file in ..\PyPoll\Resources.
election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# This function will create a dict of unique candidates but will also increment the value field for the candidates.
def count_candidate_votes(csv):
    election_data = {}
    for row in csv:
        if row[2] not in election_data:
            election_data[row[2]] = 0
        election_data[row[2]] += 1
    return(election_data)

# Open the CSV and read the data into a list of individual votes
with open(election_csv, 'r', newline='') as election_data:
    csv_reader = csv.reader(election_data, delimiter=",")
    csv_header = next(csv_reader)
    votes = [row for row in csv_reader]

# Open the dir where we will output the results
with open("PyPoll\\Analysis\\results.txt", "w", newline='') as output:   
    
    # Creates a list of candidates generated from the function
    candidates = list(count_candidate_votes(votes).keys())

    # Creates a list of candidate vote totals generated from the function
    candidate_votes = list(count_candidate_votes(votes).values())
    
    print(f"""\n
    Election Results
    -------------------------
    Total Votes: {sum(candidate_votes)}
    -------------------------
    {candidates[0]}: {(candidate_votes[0] / sum(candidate_votes)):.3%} ({candidate_votes[0]})
    {candidates[1]}: {(candidate_votes[1] / sum(candidate_votes)):.3%} ({candidate_votes[1]})
    {candidates[2]}: {(candidate_votes[2] / sum(candidate_votes)):.3%} ({candidate_votes[2]})
    -------------------------
    Winner: {max(count_candidate_votes(votes), key=itemgetter(1))}
    -------------------------
    """)


    output.write(f"""   
    Election Results
    -------------------------
    Total Votes: {sum(candidate_votes)}
    -------------------------
    {candidates[0]}: {(candidate_votes[0] / sum(candidate_votes)):.3%} ({candidate_votes[0]})
    {candidates[1]}: {(candidate_votes[1] / sum(candidate_votes)):.3%} ({candidate_votes[1]})
    {candidates[2]}: {(candidate_votes[2] / sum(candidate_votes)):.3%} ({candidate_votes[2]})
    -------------------------
    Winner: {max(count_candidate_votes(votes), key=itemgetter(1))}
    
    """)