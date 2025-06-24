contacts = {}
choice = ""

while choice != "5":
    print("\n1. Add\n2. View\n3. Update\n4. Delete\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        contacts[name] = number

    elif choice == "2":
        for name in contacts:
            print(name + ":", contacts[name])

    elif choice == "3":
        name = input("Enter name to update: ")
        if name in contacts:
            number = input("Enter new number: ")
            contacts[name] = number
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
        else:
            print("Contact not found.")
