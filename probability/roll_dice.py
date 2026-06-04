"""simulate a casino where two dice are rolled together,
 and the player wins if there are two six and gets $100.
What will be the average profit if the casino fee is 5 cents per game"""

import random


def simulate_roll():
    """simulate roll and return the number"""
    return random.randint(1, 6)


def roll_dice():
    """roll 2 dice and update earnings"""
    dice_1 = simulate_roll()
    dice_2 = simulate_roll()

    if dice_1 == 6 and dice_2 == 6:
        return 100
        # print("Hurrayyyyyy")
    else:
        return 0


def casino_simulation(number_of_trials):
    """Simulate multiple trials of rolling 2 dice"""
    casino_revenue = 0
    for _ in range(number_of_trials):
        casino_revenue += 0.05
        # casino_revenue += 2.78 #BreakEven fee
        casino_revenue -= roll_dice()

    average_casino_profit = (casino_revenue) / number_of_trials
    print("Casino Revenue:", round(casino_revenue, 2))
    print(
        f"Avg earning from {number_of_trials} players is :{round(average_casino_profit, 2)}"
    )


TRIAL_CT = 500000
casino_simulation(TRIAL_CT)
