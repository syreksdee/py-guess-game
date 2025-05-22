import random
lower_bound = 1
upper_bound = 100
secret_number = random.randint(lower_bound, upper_bound)
number_of_guesses = 0
print(f"I'm thinking of a number between {lower_bound} and {upper_bound}")

while True:
    try:
        user_guess_str = input("Take a guess: ")
        user_guess = int(user_guess_str)

        number_of_guesses += 1
        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it! The number was {secret_number}.")
            print(f"It took you {number_of_guesses} guesses.")
            break

    except ValueError:
        print("Oops! That is not a valid number. Please enter a number.")
