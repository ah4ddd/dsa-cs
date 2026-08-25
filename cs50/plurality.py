# Ask for candidates
candidates = input("Enter candidate names separated by spaces: ").split()

# Create a dictionary with every candidate starting at 0 votes
votes = {}

for candidate in candidates:
    votes[candidate] = 0


# Ask for number of voters
voter_count = int(input("Number of voters: "))


# Collect votes
for i in range(voter_count):
    name = input("Vote: ")

    if name in votes:
        votes[name] += 1
    else:
        print("Invalid vote.")


# Find highest number of votes
max_votes = max(votes.values())


# Print all candidates with the highest number
for candidate in votes:
    if votes[candidate] == max_votes:
        print(candidate)
