import random


def number_guessing_game():
    print("Number Guessing Game")
    print("I have chosen a number between 1 and 100.")
    print("You have to guess the number within 10 attempts.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while attempts < 10:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if guess == secret_number:
            print(
                f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

    if attempts == 10:
        print(
            f"Sorry, you have reached the maximum number of attempts. The correct number was {secret_number}.")


if __name__ == "__main__":
    number_guessing_game()
