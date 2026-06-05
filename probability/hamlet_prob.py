"""Infinte monkey Theorem.The infinite monkey theorem states that
a monkey hitting keys at random on a typewriter keyboard for
an infinite amount of time will almost surely type any given text,
such as the complete works of William Shakespeare.
Write a function that calculates the probability of writing the
title "Hamlet, containing 130,000  letters , ignoring capital and punctuation"
"""


def compute_probability(title):
    """Compute and return probability of picking a letter from A-Z"""
    letter_count = len(title)
    title_probability = (1 / 26) ** letter_count
    return title_probability


TITLE = "HAMLET"
probability_of_typing_title = compute_probability(TITLE)

print(f"Probability to type {TITLE} is {probability_of_typing_title}")
