'''

Here's a simple Python program that takes 
two numbers and an operator as input and 
performs the corresponding operation:
'''


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."


def calculator():
    print("Simple Calculator")
    print("Enter two numbers and an operator (+, -, *, /)")

    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        result = "Invalid operator"

    print(f"Result: {result}")


if __name__ == "__main__":
    calculator()


'''


'''
