print("Welcome")
print("===== CHATBOT =====")
print("Type 'bye' to end chat")

while True:

    user = input("You : ")
    user = user.lower()

    if user == "hi" or user == "hello":
        print("Bot : Hello!")

    elif user == "how are you":
        print("Bot : I am fine. What about you?")

    elif user == "i am feeling good":
        print("Bot : Nice to hear ")

    elif user == "what is your name":
        print("Bot : My name is JARVIS")

    elif user == "who made you":
        print("Bot : I am created using Python")
        
    elif user == "are you a ai":
        print("Bot : I am a simple ChatBot Ai Based")    
        

    elif user == "bye":
        print("Bot : Goodbye")
        break

    else:
        print("Bot : Sorry, I don't understand")
