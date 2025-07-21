import re

def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Chatbot: Goodbye! Have a nice day.")
            break

        
        elif re.search(r"\b(hi|hello|hey)\b", user_input):
            print("Chatbot: Hello there! How can I help you?")

        
        elif re.search(r"\b(your name|who are you)\b", user_input):
            print("Chatbot: I'm a rule-based chatbot made with Python.")

  
        elif "help" in user_input:
            print("Chatbot: I can help you with basic queries like greetings, FAQs, and more!")

       
        elif re.search(r"\b(how are you)\b", user_input):
            print("Chatbot: I'm just a program, but I'm doing great!")

        elif re.search(r"\b(what can you do|features)\b", user_input):
            print("Chatbot: I can respond to greetings, tell you who I am, offer help, and answer simple FAQs.")

        else:
            print("Chatbot: I'm sorry, I didn't understand that. Type 'help' to see what I can do.")

# Run the chatbot
chatbot()
