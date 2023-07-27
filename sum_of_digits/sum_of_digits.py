def sum_of_digits(number):
    # Convert the number to a string to access individual digits
    num_str = str(number)

    # Initialize the sum of digits to 0
    digit_sum = 0

    # Iterate through each digit and add it to the sum
    for digit in num_str:
        digit_sum += int(digit)

    return digit_sum


if __name__ == "__main__":
    try:
        num = int(input("Enter an integer to calculate the sum of its digits: "))
        digit_sum_result = sum_of_digits(num)
        print(f"Sum of digits of {num}: {digit_sum_result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
