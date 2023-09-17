# Guessing game!

import random

low = 1
high = 50

correct_answer = random.randint(low, high)

print(f"Guess a number within this range ({low} to {high}): ")

for attempt in range(5):
    guess = int(input(f"Attempt {attempt + 1}: "))

    if guess < correct_answer:
        print("Correct answer is greater!")
    elif guess > correct_answer:
        print("Correct answer is smaller!")
    else:
        print("You Win!")
        break
else:
    print(f"You lose! Correct answer is: {correct_answer}")