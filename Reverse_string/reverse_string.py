def reverse_string(input_string):
    # Using slicing to reverse the string
    reversed_string = input_string[::-1]
    return reversed_string


if __name__ == "__main__":
    try:
        string_to_reverse = input("Enter a string to reverse: ")
        reversed_string_result = reverse_string(string_to_reverse)
        print(f"Reversed string: {reversed_string_result}")
    except ValueError:
        print("Invalid input. Please enter a valid string.")
