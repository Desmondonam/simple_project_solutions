import random


def roll_dice(num_dice, num_sides):
    results = []
    for _ in range(num_dice):
        result = random.randint(1, num_sides)
        results.append(result)
    return results


def display_results(results):
    print("Dice Roll Results:")
    for index, result in enumerate(results, 1):
        print(f"Die {index}: {result}")


def dice_rolling_simulator():
    print("Welcome to the Dice Rolling Simulator!")
    try:
        num_dice = int(input("Enter the number of dice to roll: "))
        num_sides = int(input("Enter the number of sides on each die: "))

        if num_dice <= 0 or num_sides <= 0:
            print("Number of dice and sides must be positive integers.")
        else:
            results = roll_dice(num_dice, num_sides)
            display_results(results)
    except ValueError:
        print("Invalid input. Please enter valid positive integers for the number of dice and sides.")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")


if __name__ == "__main__":
    dice_rolling_simulator()
