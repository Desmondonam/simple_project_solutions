'''
Python code to check if a number is prime
'''


def is_prime(number):
    # Prime numbers are greater than 1
    if number <= 1:
        return False

    # Check for divisibility from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    # If the number is not divisible by any smaller number, it is prime
    return True


if __name__ == "__main__":
    try:
        num = int(input("Enter a number to check if it's prime: "))
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
