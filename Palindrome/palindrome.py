def is_palindrome(word):
    # Remove spaces and convert to lowercase
    cleaned_word = ''.join(word.lower().split())

    # Check if the word is equal to its reverse
    return cleaned_word == cleaned_word[::-1]


if __name__ == "__main__":
    try:
        word = input("Enter a word to check if it's a palindrome: ")
        if is_palindrome(word):
            print(f"{word} is a palindrome.")
        else:
            print(f"{word} is not a palindrome.")
    except Exception as e:
        print(f"An error occurred: {e}")
