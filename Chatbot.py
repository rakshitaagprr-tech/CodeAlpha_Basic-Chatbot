def chatbot():
    print("🤖 Welcome to the Basic Chatbot!")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "hi":
            print("Bot: Hello! How can I help you?")

        elif user == "how are you":
            print("Bot: I'm fine, thanks! How about you?")

        elif user == "what is your name":
            print("Bot: I am a Python Chatbot.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Start the chatbot
chatbot()
