users = {
    "Amit": {"cricket", "music", "coding", "movies"},
    "Rahul": {"football", "music", "travel", "coding"},
    "Neha": {"reading", "music", "art", "travel"},
    "John": {"gaming", "coding", "movies", "music"},
}


def find_common_interests(user1, user2):
    set1 = users[user1]
    set2 = users[user2]

    common = set1 & set2  # intersection

    return common


# Input
u1 = input("Enter first user: ")
u2 = input("Enter second user: ")

result = find_common_interests(u1, u2)

print("\nCommon Interests between", u1, "and", u2)
print(result)
