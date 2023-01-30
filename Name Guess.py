import random

print("Welcome to the number guessing game!")
print("Guess a number between 1 and 100")

# Generate a random number between 1 and 100
answer = random.randint(1, 100)

# Keep track of the number of guesses
guesses = 0

# Start the guessing loop
while True:
    # Get the player's guess
    guess = int(input("Your guess: "))
    guesses += 1

    # Check if the player's guess is too high, too low, or correct
    if guess < answer:
        print("Too low, try again")
    elif guess > answer:
        print("Too high, try again")
    else:
        print(f"Correct! You took {guesses} guesses.")
        break
