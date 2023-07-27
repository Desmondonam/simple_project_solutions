def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


if __name__ == "__main__":
    try:
        print("Temperature Converter Menu:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")
        elif choice == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")
        else:
            print("Invalid choice. Please select 1 or 2.")

    except ValueError:
        print("Invalid input. Please enter a valid temperature value.")
