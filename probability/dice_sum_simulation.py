"""Compute probability that when rolling two six-sided dice, their
sum equals a specific value (e.g., 7)?"""

import random


def roll_value():
    """simulate rolling of 1 dice"""
    return random.randint(1, 6)


def roll_dice():
    """simulate rolling of 2 dice and return result"""
    dice_1 = roll_value()
    dice_2 = roll_value()
    return dice_1 + dice_2


def dice_sum_simulation(n, no_of_trials):
    """compute probability of sum of rolling 2 dice"""
    sucess = 0
    for _ in range(no_of_trials):
        sum_of_dice = roll_dice()
        if sum_of_dice == n:
            sucess += 1
    prob_of_sum_n = sucess / no_of_trials
    return prob_of_sum_n


def all_pairings():
    """Sample space of rolling 2 six sided dice is returned as list of tuples"""
    total_pairings = []
    for i in range(1, 7):
        for j in range(1, 7):
            total_pairings.append((i, j))
    return total_pairings


# ------Below functions are for Theorital calculation * BEGIN *------
def fn_sample_space(n, total_pairings):
    """find sample space where sum of 2 dice is equal to n"""
    sample_space = []
    for ele in total_pairings:
        if ele[0] + ele[1] == n:
            sample_space.append(ele)
    return sample_space


def dice_sum_theoritical_probability(n):
    """compute probability of sum of rolling 2 dice"""
    pairs = all_pairings()
    event_space_size = len(pairs)
    sample_space_pairs = fn_sample_space(n, pairs)
    sample_space_size = len(sample_space_pairs)
    prob_of_sum_n = sample_space_size / event_space_size
    print("Sample Space", sample_space_pairs)
    return prob_of_sum_n


# ------Below functions are for Theorital calculation * END *------

SUM_OF_DICE = 12
NO_OF_TRIAL_SIMULATIONS = 10000
PROB_FROM_SIMULATION = dice_sum_simulation(SUM_OF_DICE, NO_OF_TRIAL_SIMULATIONS)
THEOROTIACAL_PROBABILITY = dice_sum_theoritical_probability(SUM_OF_DICE)
print(
    f"Simulation Probability of sum of 2 dice roll of :{SUM_OF_DICE} is :{PROB_FROM_SIMULATION}"
)
print(
    f"Theorotiacal Probability of sum of 2 dice roll of :{SUM_OF_DICE} is :{THEOROTIACAL_PROBABILITY}"
)
