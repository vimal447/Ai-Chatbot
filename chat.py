import random
import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responsesh
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you! How about you?", "I'm just a bot, but I'm good!"]
    ],
    [
        r"(.*) your name?",
        ["I'm a chatbot, you can call me ChatBot!", "I don't have a name, but you can call me AI!"]
    ],
    [
        r"quit|bye",
        ["Goodbye! Have a great day!", "Bye! Talk to you later!"]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that.", "Can you rephrase that?", "Interesting... Tell me more!"]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "quit"]:
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chat()
