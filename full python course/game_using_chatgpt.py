import random

# generate a random number between 1 and 20
secret_number = random.randint(1, 20)

# set the number of guesses allowed
guesses_remaining = int(input("How many guesses would you like? "))

# loop until the player runs out of guesses or guesses the correct number
while guesses_remaining > 0:
    # get the player's guess
    guess = int(input("Guess a number between 1 and 20: "))
    
    # check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the secret number.")
        break
    
    # provide a hint if the guess is too high or too low
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Too low!")
    
    # decrement the number of guesses remaining
    guesses_remaining -= 1
    continue

# if the player runs out of guesses, reveal the secret number
if guesses_remaining == 0:
    print(f"Sorry, you ran out of guesses. The secret number was {secret_number}.")
