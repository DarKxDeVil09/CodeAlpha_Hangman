def simple_chatbot():
    print("--- CodeAlpha Basic Chatbot ---")
    print("Bot: Hello! I am a simple rule-based bot. (Type 'bye' to exit)")

    while True:
        # Get user input and convert to lowercase for easier matching
        user_input = input("You: ").lower()

        # Rule-based logic using if-elif-else
        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hi there! How can I help you today?")
            
        elif "how are you" in user_input:
            print("Bot: I'm just a program, but I'm running perfectly! How about you?")
            
        elif "your name" in user_input:
            print("Bot: I am the CodeAlpha Task Bot.")
            
        elif "python" in user_input:
            print("Bot: Python is a great language! Are you enjoying your internship?")
            
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a great day!")
            break  # Stop the loop
            
        else:
            print("Bot: I'm sorry, I don't understand that yet. Can you try saying 'hello'?")

if __name__ == "__main__":
    simple_chatbot()