import random

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Chatbot: Goodbye!")
        break

    elif "hello" in user or "hi" in user or "hey" in user:
        print("Chatbot:", random.choice(["Hello!", "Hi there!", "Hey!"]))

    elif "how are you" in user:
        print("Chatbot:", random.choice(["I'm fine!", "Doing great!", "All good!"]))

    elif "name" in user:
        print("Chatbot: I'm a Python chatbot.")

    elif "help" in user:
        print("Chatbot: You can greet me or ask simple questions!")

    elif "your creator" in user or "who made you" in user:
        print("Chatbot: I was created using Python.")

    else:
        print("Chatbot:", random.choice([
            "I don't understand.",
            "Can you say that differently?",
            "Hmm, interesting!"
        ]))