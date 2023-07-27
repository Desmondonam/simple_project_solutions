def show_menu():
    print("Shopping List Menu:")
    print("1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Exit")


def add_item(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the shopping list.")


def view_list(shopping_list):
    print("Shopping List:")
    if not shopping_list:
        print("The list is empty.")
    else:
        for index, item in enumerate(shopping_list, 1):
            print(f"{index}. {item}")


def remove_item(shopping_list):
    view_list(shopping_list)
    try:
        item_number = int(input("Enter the number of the item to remove: "))
        if 1 <= item_number <= len(shopping_list):
            removed_item = shopping_list.pop(item_number - 1)
            print(f"{removed_item} removed from the shopping list.")
        else:
            print("Invalid item number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid item number.")


if __name__ == "__main__":
    shopping_list = []

    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            view_list(shopping_list)
        elif choice == "3":
            remove_item(shopping_list)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
