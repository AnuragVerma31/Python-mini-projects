expenses = []  # list

while True:  # using loop to show input options
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")  # enter input option (1-4)

    if choice == "1":  # if input is 1 adds expense
        date = input("Enter date (DD-MM-YYYY): ")
        name = input("Enter expense name: ")
        type = input("Enter type (Food/Travel/etc): ")
        amount = float(input("Enter amount: "))
        expenses.append([date, name, type, amount])
        print("Added!")

    elif choice == "2":  # if input is 2 shows expenses
        print("\nExpenses List:")
        for e in expenses:
            print(e[0], "-", e[1], "-", e[2], "-", e[3])

    elif choice == "3":  # if input is 3 shows total expense
        total = 0
        for e in expenses:
            total = total + e[3]
        print("Total Expense:", total)

    elif choice == "4":  # if input is 4(exit)
        print("Exit")
        break

    else:
        print("Wrong choice")  # prints wrong choice if something went wrong
