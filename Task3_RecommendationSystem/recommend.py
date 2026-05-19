# Movie Recommendation System

movies = {
    "action": ["KGF", "Pushpa", "War", "Pathaan"],
    "comedy": ["Golmaal", "Dhamaal", "Hera Pheri", "Welcome"],
    "romance": ["DDLJ", "Ashiqui 2", "Sita Ramam", "Jab We Met"],
    "horror": ["Stree", "Conjuring", "Bhool Bhulaiyaa", "Annabelle"]
}

print("===================================")
print("    MOVIE RECOMMENDATION SYSTEM")
print("===================================")

name = input("Enter your name : ")

print()
print("Hello", name)

while True:

    print()
    print("Available Categories")
    print("1. Action")
    print("2. Comedy")
    print("3. Romance")
    print("4. Horror")
    print("5. Exit")

    choice = input("Enter category : ")
    choice = choice.lower()

    if choice == "action":

        print()
        print("Recommended Action Movies")

        for i in movies["action"]:
            print("-", i)

    elif choice == "comedy":

        print()
        print("Recommended Comedy Movies")

        for i in movies["comedy"]:
            print("-", i)

    elif choice == "romance":

        print()
        print("Recommended Romance Movies")

        for i in movies["romance"]:
            print("-", i)

    elif choice == "horror":

        print()
        print("Recommended Horror Movies")

        for i in movies["horror"]:
            print("-", i)

    elif choice == "exit":

        print()
        print("Thank You For Using Recommendation System")
        break

    else:

        print()
        print("Invalid Category")
