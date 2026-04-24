visitors = []  # set

while True:  # taking input
    name = input("Enter visitor name (or type 'exit'): ")

    if name.lower() == "exit":
        break

    visitors.append(name)

unique_visitors = set(visitors)

print("\n--- Visitor Report ---")  # prints report
print("All Entries:", visitors)
print("Unique Visitors:", unique_visitors)
print("Total Visits:", len(visitors))
print("Unique Visitors Count:", len(unique_visitors))
