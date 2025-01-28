import random


responses = {
    "hello": ["Hi there! 😊", "Hello! How can I assist you?", "Hey! What's up?"],
    "how are you": [
        "I'm feeling chatty today! How about you?", 
        "I'm just a bot, but I'm here to make your day better. And you?",
        "Doing great! Ready to help you out!"
    ],
    "bye": ["Goodbye! Take care! 👋", "See you later! 😄", "Bye! Have a wonderful day!"],
    "your name": [
        "I'm Chatboticus, your virtual friend!", 
        "I don't have a formal name, but you can call me 'ChatMaster 3000.'",
        "Just call me your friendly helper!"
    ],
    "joke": [
        "Why did the scarecrow win an award? Because he was outstanding in his field! 😄",
        "What do you call fake spaghetti? An impasta! 🍝",
        "Why don't skeletons fight each other? They don't have the guts! 🦴"
    ],
}
 
def chatbot_response(user_input):
    user_input = user_input.lower()


    if "hello" in user_input:
        return random.choice(responses["hello"])
    elif "how are you" in user_input:
        return random.choice(responses["how are you"])
    elif "bye" in user_input:
        return random.choice(responses["bye"])
    elif "your name" in user_input:
        return random.choice(responses["your name"])
    elif "joke" in user_input:
        return random.choice(responses["joke"])
    elif "game" in user_input:
        return "Let's play a guessing game! Think of a number between 1 and 10, and I'll try to guess it!"
    else:
        return "Hmm, I didn't catch that. Could you try saying it differently? 😊"


def chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot. Ask me anything or just say 'joke' for a laugh!")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot:", random.choice(responses["bye"]))
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")


chatbot()