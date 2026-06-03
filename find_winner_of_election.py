"""Given a list of votes where each element represents a vote for a candidate,
determine the winner of the election. If multiple candidates receive the
same number of maximum votes, the candidate with the lexicographically smaller name
should be declared the winner."""

from collections import Counter

votes = [
    "john",
    "johnny",
    "jackie",
    "johnny",
    "john",
    "jackie",
    "jamie",
    "jamie",
    "john",
    "johnny",
    "jamie",
    "johnny",
    "john",
]
votes_counter=Counter(votes)
max_votes=votes_counter.most_common(1)[0][1] #[('john', 4)] list of tupple .

names=[ele[0] for ele in votes_counter.items() if ele[1]==max_votes]
print(sorted(names)[0])