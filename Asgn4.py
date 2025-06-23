import random

# Step 1: Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Initialize variables
attempts = 0
max_attempts = 10

print("Welcome to the Number Guessing Game!")
print("Guess the number (between 1 and 100). You have 10 attempts!")

# Step 2: Prompt the user for guesses
while attempts < max_attempts:
    try:
        # Get the user's guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check the guess
        if guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            break
    except ValueError:
        print("Please enter a valid number.")

# Step 3: Handle game over if attempts are exceeded
if attempts == max_attempts and guess != number_to_guess:
    print(f"Game over! The correct number was {number_to_guess}. Better luck next time! ")