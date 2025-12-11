def chatbot():
    print("🤖 Chatbot: Hello! I'm your Python Chatbot.")
    print("Type 'help' to see what I can do. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        
        if user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day! 👋")
            break

        
        elif user_input in ["hello", "hi", "hey"]:
            print("🤖 Chatbot: Hi! How can I help you today?")
        
        
        elif user_input in ["how are you", "how r u", "how are you?"]:
            print("🤖 Chatbot: I'm doing great! Thanks for asking 😊")
        
        
        elif user_input in ["what is your name", "who are you"]:
            print("🤖 Chatbot: I'm a simple Python chatbot created by you!")
        
        
        elif user_input in ["thanks", "thank you"]:
            print("🤖 Chatbot: You're welcome! 😄")

        elif user_input == "help":
            print("🤖 Chatbot: Here are the things I can respond to:")
            print(" - hello / hi / hey")
            print(" - how are you")
            print(" - what is your name / who are you")
            print(" - thanks / thank you")
            print(" - bye (to exit)")
        
        else:
            print("🤖 Chatbot: Sorry, I don't understand that. Try 'help' to see commands.")


chatbot()
