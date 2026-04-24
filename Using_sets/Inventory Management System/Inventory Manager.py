# Initial stock (set automatically removes duplicates)
inventory = {"pen", "pencil", "eraser", "notebook", "marker"}

sold_items = set()


def show_inventory():
    print("\nAvailable Items:", inventory)
    print("Sold Items:", sold_items)


def sell_item(item):
    if item in inventory:
        inventory.remove(item)
        sold_items.add(item)
        print(item, "sold successfully")
    else:
        print(item, "not available in stock")


def add_item(item):
    inventory.add(item)
    print(item, "added to stock")


# Menu system
while True:
    print("\n1. Show Inventory")
    print("2. Sell Item")
    print("3. Add Item")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_inventory()

    elif choice == "2":
        item = input("Enter item to sell: ")
        sell_item(item)

    elif choice == "3":
        item = input("Enter item to add: ")
        add_item(item)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
