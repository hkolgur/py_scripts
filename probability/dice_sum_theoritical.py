"""Theoritacially compute dice sum probability"""

def all_pairings():
    """Sample space of rolling 2 six sided dice is returned as list of tuples"""
    total_pairings = []
    for i in range(1, 7):
        for j in range(1, 7):
            total_pairings.append((i, j))
    return total_pairings


def fn_sample_space(n, total_pairings):
    """find sample space where sum of 2 dice is equal to n"""
    sample_space = []
    for ele in total_pairings:
        if ele[0] + ele[1] == n:
            sample_space.append(ele)
    return sample_space


def dice_sum_probability(n):
    """compute probability of sum of rolling 2 dice"""
    pairs = all_pairings()
    event_space_size = len(pairs)
    sample_space_pairs = fn_sample_space(n, pairs)
    sample_space_size = len(sample_space_pairs)
    prob_of_sum_n = sample_space_size / event_space_size
    print("Sample Space", sample_space_pairs)
    return prob_of_sum_n


SUM_OF_DICE = 7
prob = dice_sum_probability(SUM_OF_DICE)
print(f"probability of sum of 2 dice roll of :{SUM_OF_DICE} is :{prob}")
