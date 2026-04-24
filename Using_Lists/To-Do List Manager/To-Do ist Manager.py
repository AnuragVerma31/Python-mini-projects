tasks = []  # List

while True:  # using loop to print options
    print("\n1. Add  2. Show  3. Delete  4. Exit")

    choice = input("Enter choice: ")  # takes input

    if choice == "1":  # if input is 1 adds task
        task = input("Enter task: ")
        time = input("Enter time: ")
        tasks.append([task, time])
        print("Added")

    elif choice == "2":  # if input is 2 shows tasks
        for t in tasks:
            print(t[0], "-", t[1])

    elif choice == "3":  # if input is 3 deletes task
        for i in range(len(tasks)):
            print(i + 1, tasks[i][0], "-", tasks[i][1])

        n = int(input("Delete number: "))
        tasks.pop(n - 1)
        print("Deleted")

    elif choice == "4":  # if input is 4 exits
        break

    else:  # using else condition to pring wrong choice if something went wrong
        print("Wrong choice")
