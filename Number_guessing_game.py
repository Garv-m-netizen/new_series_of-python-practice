import random
number=random.randint(1,100)
attempts=0
max_attempts=7
print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 to 100: ")
while attempts<max_attempts:
    try:
        guess=int(input(f"Attempt{attempts+1}: Enter your guess: "))
        attempts+=1
        if guess==number:
            print("Congratulations! you're right")
            break
        elif guess<number:
            print("Too low!")
        else:
            print("Too high!")

    except ValueError:
        print("Please enter a valid number")
if attempts==max_attempts and guess!=number:
    print(f"out of attempts! The number was {number}")