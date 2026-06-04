"""Determine whether to accept a coin-tossing bet
based on its expected return .A game consists of flipping
a fair coin repeatedly until a Head (H) appears,
at which point the game immediately terminates.
For every Tail (T) flipped before the head,
you must pay your friend $10.
When the Head finally appears, your friend pays you $100."""

import random

def coin_toss():
    """Simulates head or tail coin toss ,
    stop when you hit a heads"""
    sum = 0
    while True:
        flip=random.choice(['H','T'])
        if flip=='H':
            sum += 100
            break
        else:
            sum -= 10
            #print(f"New sum is :{sum}")
    return sum

def simulate_trails(trial_ct):
    """Simulate coin flip trial multiple times"""
    trail_earning=0
    for tr_num in range(trial_ct):
        trail_earning += coin_toss()
        #print(f"Trail {tr_num} earning is :{trail_earning}")
    average_earning = trail_earning / trial_ct
    print(f"Average Amount earned: {average_earning}")

TRIAL_CT = 100000
simulate_trails(TRIAL_CT)
