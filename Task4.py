
def chatbot():
    print("Chatbot: Hello! Welcome to my chatbot.")
    print("Chatbot: You can say hello, how are you,what is your name  or bye.")

    while True:
        user_input = input("You: ")
        if user_input == "hello":
            print("Chatbot: Hi!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Chatbot: I am a simple Python chatbot.")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()
