def chatbot():
    print("ChatBot: Hi! Type 'bye' to exit:")
    while True:
        user = input("You: ").lower().strip()
        if user == "hello":
            print("ChatBot: Hi!")
        elif user == "how are you":
            print("ChatBot: I'm fine, thanks what about you?")
        elif user == "what is your name":
            print("ChatBot: I'm a simple python chatbot.")
        elif user == "bye":
            print("ChatBot: GoodBye!")
            break
        else:
            print("ChatBot: sorry, I don't understand that.")
chatbot()