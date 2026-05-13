import re

def chatbot_response(query):
    faqs = {
        "what is your name": "I am a FAQ Bot.",
        "how can you help me": "You can ask me any FAQ.",
        "what can you do": "I can answer simple questions based on predefined answers.",
        "bye": "Goodbye! Have a nice day!",
    }
    for key in faqs:
        if re.search(key, query.lower()):
            return faqs[key]
    return "Sorry, I don't understand."

# Chatbot loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Bot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Bot:", response)
