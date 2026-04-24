contacts = []  # list

while True:  # useing while loop to print options
    print("\n1. Add Contact")
    print("2. Show Contacts")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input("Enter choice: ")  # taking input

    if choice == "1":  # if input is 1 adds contact
        name = input("Enter name: ")
        number = input("Enter number: ")
        contacts.append([name, number])
        print("Added")

    elif choice == "2":  # if input is 2 shows contacts
        for c in contacts:
            print(c[0], "-", c[1])

    elif choice == "3":  # if input is 3 deletes contact
        for i in range(len(contacts)):
            print(i + 1, contacts[i][0], "-", contacts[i][1])

        n = int(input("Delete number: "))
        contacts.pop(n - 1)
        print("Deleted")

    elif choice == "4":  # if input is 4 exit
        break

    else:  # if something wents wrong prints wrong choice
        print("Wrong choice")
