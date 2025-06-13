import random
import re

intents ={
    "greetings":{
        "patterns":["hello", "hi", "hey"],
        "responses":["Hi!", "Hey, there"]
    },
    "goodbyes":{
        "patterns":["Bye", "Goodbye"],
        "responses":["Bye!", "Goodbye!"]
    },
    "thanks":{
        "patterns":["Thank you!", "Thanks"],
        "responses":["You're Welcome!", "No Problem!"]
    },
    "questions":{
        "How are you":["I am fine, thanks!", "I am good!"]

    }
}

def match_intent(user_input):
    for intent, intent_data in intents.items():
        if isinstance(intent_data, dict) and "patterns" in intent_data:
            for pattern in intent_data["patterns"]:
                if re.search(pattern, user_input, re.IGNORECASE):
                    return random.choice(intent_data["responses"])

    for question, responses in intents["questions"].items():
        if re.search(question, user_input, re.IGNORECASE):
            return random.choice (responses)

    return None
def get_response(user_input):
    matched_intent = match_intent(user_input)

    if matched_intent:
        return matched_intent
    else:
        return "Sorry, I didn't understand your query."

def chatbot():
    print("Welcome to the chatbot.")

    while True:
        user_input = input("You:")

        if "bye" in user_input.lower():
            print("Chatbot:Goodbye!")
            break

        response = get_response(user_input)
        print("Chatbot :", response)

chatbot()