"""Take a guess from user to match the random number generated"""

import random

answer = random.randint(1, 100)
guess_count = 0

while True:
    try:
        user_guess = int(input("Enter a number between 1 and 100:"))
        guess_count += 1
    except ValueError:
        print("Invalid input.. Enter numbers")
        continue
    if user_guess < 1 or user_guess > 100:
        continue
    elif user_guess == answer:
        print(f"Entered number:{user_guess}, expected number{answer}")
        break
    elif user_guess > answer:
        print("Too High Try agian...")
        continue
    elif user_guess < answer:
        print("Too low try again..")

print(f"Total guesses:{guess_count}")
