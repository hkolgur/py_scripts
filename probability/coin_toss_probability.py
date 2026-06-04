"""Simulate cointoss of 100 coins n number of times .
Compute average probability of H/T"""

import random


def coin_toss():
    """Return head based on random function value."""
    # random.random() cutoff- 0.5 is exactly a 50% chance
    if random.random() < 0.5:
        return 1
    return 0


def coin_trial(coins_ct):
    """Perform trial and return heads count."""
    heads_count = 0
    for _ in range(coins_ct):
        heads_count += coin_toss()
    return heads_count


def simulate(trial_count, coin_count):
    """Simulates multi trial coin tosses. Prints average Heads count and probability."""
    total_heads = 0
    for _ in range(trial_count):
        total_heads += coin_trial(coin_count)

    # Calculate metrics
    avg_heads = total_heads / trial_count
    avg_probability = avg_heads / coin_count  # Fixes the probability math

    print(f"Average Heads per trial: {round(avg_heads, 4)} in {coin_count} coins ")
    print(f"Average Heads Probability: {round(avg_probability, 4)}")


simulate(2000, 1000)
