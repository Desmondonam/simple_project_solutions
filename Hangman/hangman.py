import random


def choose_word():
    word_list = ["apple", "banana", "cherry",
                 "grape", "orange", "watermelon", "pineapple"]
    return random.choice(word_list)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def get_guess(guessed_letters):
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif not guess.isalpha():
            print("Please enter a valid letter.")
        elif guess in guessed_letters:
            print("You've already guessed that letter. Try a different one.")
        else:
            return guess


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    max_attempts = 6

    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")

    while max_attempts > 0:
        display = display_word(word, guessed_letters)
        print("\n" + display)

        if "_" not in display:
            print("Congratulations! You guessed the word:", word)
            break

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess not in word:
            max_attempts -= 1
            print(
                f"Wrong! '{guess}' is not in the word. You have {max_attempts} attempts left.")

    if max_attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", word)


if __name__ == "__main__":
    play_hangman()
