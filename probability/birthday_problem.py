"""birthday problem explores the likelihood that in a randomly selected
group of people, there exists at least one pair who share the same birthday
(day and month, but not necessarily the same year).
Calculate this probability"""


def no_overlap_probabiity(n):
    """compute probability of each person having different birthday, then
    compute atleast one has matching birthday. Return matching prob"""

    prob_none_with_sameday = 1

    for i in range(n):
        prob_none_with_sameday *= (365 - i) / 365
    return prob_none_with_sameday


def atleast_one_overlap(n):
    """compute probabiity of atleast one overlap"""
    if n <= 1:
        print("Enter number above 1 ")
        overlap = 0
    elif n > 365:
        overlap = 1
    else:
        overlap = 1 - (no_overlap_probabiity(n))

    print(f"probability of atleast one overlap from gorup of {n} is: {overlap}")


atleast_one_overlap(35)
