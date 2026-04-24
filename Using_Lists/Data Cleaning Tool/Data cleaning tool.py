data = []  # list

while True:  # using while loop to print options
    print("\n1. Add Data")
    print("2. Clean Data")
    print("3. Show Data")
    print("4. Exit")

    choice = input("Enter choice: ")  # takes input

    if choice == "1":  # if input is 1 adds data
        value = input("Enter value: ")
        data.append(value)

    elif choice == "2":  # if inout is 2 cleans data
        clean_data = []

        for d in data:
            d = d.strip()

            # remove unwanted values
            if d != "" and d != "NA" and d != "NULL":
                if d not in clean_data:
                    clean_data.append(d)

        data = clean_data
        print("Data cleaned")

    elif choice == "3":  # if input is 3 shows data
        for d in data:
            print("-", d)

    elif choice == "4":  # if input is 4 exit
        break

    else:  # if something went wrong prints wrong choice
        print("Wrong choice")
