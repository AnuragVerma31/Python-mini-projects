# Spam keywords (set for fast lookup)
spam_keywords = {
    "free",
    "win",
    "winner",
    "cash",
    "prize",
    "loan",
    "credit",
    "offer",
    "click",
    "urgent",
}


def check_spam(email):
    email_words = set(email.lower().split())

    # Find matching spam words
    matched_words = email_words & spam_keywords

    # Decision logic
    if len(matched_words) >= 2:
        return "SPAM EMAIL", matched_words
    else:
        return "NOT SPAM", matched_words


# Input
email = input("Enter email text: ")
result, words = check_spam(email)

print("\nResult:", result)
print("Matched Spam Words:", words)
