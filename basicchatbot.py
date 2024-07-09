from datetime import datetime
from nltk.chat.util import Chat, reflections

# Define patterns for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'How can I help you?']),
    (r'how are you', ['I am good, thank you!', 'I am a chatbot, so I don\'t have feelings, but I am here to assist.']),
    (r'what is your name', ['I am a chatbot created by OpenAI.', 'You can call me ChatGPT.']),
    (r'bye|goodbye', ['Goodbye!', 'Have a great day!', 'See you later.']),
    (r'my name is (.*)', ['Nice to meet you, %1!']),
    (r'time', ['The current time is %s.' % datetime.now().strftime('%H:%M:%S')]),
    (r'interview', ['For interview tips, make sure to research the company, practice common questions, and showcase your relevant skills and experiences.']),
    (r'resume|CV', ['When preparing your resume, highlight your achievements, use action verbs, and tailor it to the job description.']),
]

# Dictionary to store user prompts and responses
user_responses = {}

# Function to add a new prompt and response to the dictionary
def add_prompt(prompt, response):
    user_responses[prompt.lower()] = response

# Create a chatbot instance
chatbot = Chat(patterns, reflections)

# Function to start the chat
def start_chat():
    print("Chatbot: Hello! I'm a text-based chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("Chatbot: Please enter a prompt (or 'bye' to exit): ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        elif user_input.lower() == 'add':
            new_prompt = input("Chatbot: Enter a new prompt: ")
            new_response = input("Chatbot: Enter a response for the prompt: ")
            add_prompt(new_prompt, new_response)
            print("Chatbot: New prompt added successfully.")
        else:
            # Check if the user input matches any prompt in the dictionary
            matched_response = user_responses.get(user_input.lower(), None)
            if matched_response:
                print("Chatbot:", matched_response)
            else:
                response = chatbot.respond(user_input)
                print("Chatbot:", response)

# Start the chat
start_chat()
