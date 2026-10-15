"""
Project 1: Rule-Based AI Chatbot
Run: python main.py
"""
from datetime import datetime

def get_response(user_input: str) -> str:
    message = user_input.lower().strip()
    if not message:
        return "Please type something so I can respond."

    # Greetings
    if message in ("hi", "hello", "hey", "good morning", "good afternoon", "good evening"):
        hour = datetime.now().hour
        if hour < 12:
            return "Hello! Good morning. How can I help you?"
        elif hour < 17:
            return "Hello! Good afternoon. How can I help you?"
        return "Hello! Good evening. How can I help you?"

    # Basic predefined rules
    elif "your name" in message or message == "name":
        return "I am RuleBot, a simple rule-based AI chatbot."
    elif "how are you" in message:
        return "I am doing well. Thanks for asking!"
    elif "help" in message:
        return "You can ask my name, how I am, or ask for a joke, time, or date."
    elif "joke" in message:
        return "Why did the computer go to the doctor? Because it had a virus!"
    elif "time" in message:
        return f"The current time is {datetime.now().strftime('%I:%M %p')}."
    elif "date" in message or "today" in message:
        return f"Today's date is {datetime.now().strftime('%d %B %Y')}."
    elif "thank" in message:
        return "You're welcome!"
    elif message in ("bye", "exit", "quit", "goodbye"):
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I don't understand that yet. Type 'help' to see what I can answer."

def main():
    print("=" * 48)
    print("       RULE-BASED AI CHATBOT (RuleBot)")
    print("Type 'help' for options and 'exit' to stop.")
    print("=" * 48)
    while True:
        user_message = input("You: ").strip()
        if user_message.lower() in ("exit", "quit", "bye", "goodbye"):
            print("RuleBot: Goodbye! Have a great day.")
            break
        print("RuleBot:", get_response(user_message))

if __name__ == "__main__":
    main()
