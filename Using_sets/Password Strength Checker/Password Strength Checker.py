def check_password_strength(password):
    upper = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lower = set("abcdefghijklmnopqrstuvwxyz")
    digits = set("0123456789")
    special = set("@$!%*?&#_")

    # Convert password into a set of characters
    pwd_set = set(password)

    score = 0

    # Check intersections
    if pwd_set & upper:
        score += 1

    if pwd_set & lower:
        score += 1

    if pwd_set & digits:
        score += 1

    if pwd_set & special:
        score += 1

    if len(password) >= 8:
        score += 1

    # Result
    if score <= 2:
        return "Weak Password"
    elif score == 3 or score == 4:
        return "Moderate Password"
    else:
        return "Strong Password"


# Input
password = input("Enter password: ")
print(check_password_strength(password))
