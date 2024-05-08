#4. Python's Random Game Night
#Task 1: Random Choice Game

import random

user_guess = int(input("Guess a number in the hidden list: "))
num = [ 5, 36, 21, 16, 10, 99, 60, 80]

random_choice = random.choice(num)
if user_guess in num:
    print("You guessed correctly!")
else:
    print("You guessed incorrectly!")