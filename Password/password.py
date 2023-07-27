import random
import string


def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    try:
        password_length = int(
            input("Enter the desired length of the password: "))
        if password_length <= 0:
            print("Password length must be a positive integer.")
        else:
            random_password = generate_random_password(password_length)
            print("Random Password:", random_password)
    except ValueError:
        print(
            "Invalid input. Please enter a valid positive integer for the password length.")
