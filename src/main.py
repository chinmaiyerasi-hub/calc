import random

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

# Generate a random number
secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
