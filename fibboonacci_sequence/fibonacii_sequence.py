'''Here's a Python program to generate the Fibonacci sequence up to a specified number of terms:'''


def fibonacci_sequence(n_terms):
    # Check if the number of terms is valid
    if n_terms <= 0:
        print("Number of terms must be a positive integer.")
        return

    # Initialize the first two terms of the sequence
    fib_sequence = [0, 1]

    # Generate the Fibonacci sequence
    for i in range(2, n_terms):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence


if __name__ == "__main__":
    try:
        num_terms = int(
            input("Enter the number of terms in the Fibonacci sequence: "))
        fibonacci_sequence_result = fibonacci_sequence(num_terms)
        print("Fibonacci Sequence:")
        print(fibonacci_sequence_result)
    except ValueError:
        print("Invalid input. Please enter a positive integer for the number of terms.")

'''The program will prompt you to enter the number of terms in the Fibonacci sequence. It will then generate and 
display the Fibonacci sequence up to the specified number of terms.'''
