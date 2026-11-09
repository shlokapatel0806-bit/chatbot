
print("Welcome to InfozaBot!")
print("Type 'bye','quit','end' to exit.")

while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user or "hey" in user:
        print("Bot: Hello! How can I help you?")

    elif "your name" in user:
        print("Bot: My name is InfozaBot.")

    elif "how are you" in user:
        print("Bot: I am fine! How are you?")

    elif "thank" in user or "thank you" in user or "thanks" in user:
        print("Bot: You're welcome!")

    elif "help" in user:
        print("Bot: I can greet you and answer your simple questions.")

    elif "bye" in user or  "quit" in user or  "end" in user:
        print("Bot: Goodbye! Have a nice day!")
        break



    else:
        print("Bot: Sorry, I don't understand. Please try again.")
