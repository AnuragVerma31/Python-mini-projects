movies = [  # list
    ["Action", "Avengers"],
    ["Action", "Fast & Furious"],
    ["Comedy", "Dhamaal"],
    ["Comedy", "Hera Pheri"],
    ["Horror", "Conjuring"],
    ["Horror", "Annabelle"],
]

print("Types: Action, Comedy, Horror")  # print types of movies

genre = input("Enter genre: ")  # takes input

print("\nRecommended Movies:")  # print recommended movies

for m in movies:
    if m[0] == genre:
        print("-", m[1])
