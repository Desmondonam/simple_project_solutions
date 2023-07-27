def show_menu():
    print("\nContact Book Menu:")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Exit")


def add_contact(contacts):
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"{name} added to the contact book.")


def view_all_contacts(contacts):
    print("\nAll Contacts:")
    if not contacts:
        print("The contact book is empty.")
    else:
        for name, contact_info in contacts.items():
            print(
                f"Name: {name}, Phone: {contact_info['Phone']}, Email: {contact_info['Email']}")


def search_contact(contacts):
    search_name = input("Enter the name of the contact to search: ")
    if search_name in contacts:
        contact_info = contacts[search_name]
        print(
            f"\nName: {search_name}, Phone: {contact_info['Phone']}, Email: {contact_info['Email']}")
    else:
        print(f"Contact '{search_name}' not found in the contact book.")


if __name__ == "__main__":
    contacts = {}

    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_all_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
