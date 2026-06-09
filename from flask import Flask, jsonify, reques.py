from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import math

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

class ChatbotLogic:
    def __init__(self):
        self.acronym_dict = {
            "API": "Application Programming Interface",
            "AI": "Artificial Intelligence",
            "CPU": "Central Processing Unit",
            "RAM": "Random Access Memory",
            "ROM": "Read-Only Memory",
            "URL": "Uniform Resource Locator",
            "HTML": "HyperText Markup Language",
            "CSS": "Cascading Style Sheets",
            "HTTP": "HyperText Transfer Protocol",
            "HTTPS": "HyperText Transfer Protocol Secure",
            "IP": "Internet Protocol",
            "DNS": "Domain Name System",
            "SQL": "Structured Query Language",
            "JSON": "JavaScript Object Notation",
            "XML": "eXtensible Markup Language",
            "IDE": "Integrated Development Environment",
            "GUI": "Graphical User Interface",
            "CLI": "Command Line Interface",
            "OOP": "Object-Oriented Programming",
            "SDK": "Software Development Kit",
            "UI": "User Interface",
            "UX": "User Experience",
            "VPN": "Virtual Private Network",
            "SSH": "Secure Shell",
            "FTP": "File Transfer Protocol",
            "IoT": "Internet of Things",
            "OS": "Operating System",
            "LAN": "Local Area Network",
            "WAN": "Wide Area Network",
            "BIOS": "Basic Input Output System",
            "CRUD": "Create, Read, Update, Delete",
            "JWT": "JSON Web Token",
            "MVC": "Model View Controller",
            "TDD": "Test Driven Development",
            "BDD": "Behavior Driven Development",
            "CI": "Continuous Integration",
            "CD": "Continuous Delivery",
            "GPU": "Graphics Processing Unit",
            "BLOB": "Binary Large Object",
            "SaaS": "Software as a Service",
            "PaaS": "Platform as a Service",
            "IaaS": "Infrastructure as a Service",
            "KPI": "Key Performance Indicator",
            "ORM": "Object Relational Mapping",
            "YAML": "YAML Ain't Markup Language",
            "ASCII": "American Standard Code for Information Interchange"
        }
        
        self.calculator_history = []

    def caesar_encrypt(self, text, shift):
        encrypted = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                encrypted += chr((ord(char) - base + shift) % 26 + base)
            else:
                encrypted += char
        return encrypted

    def caesar_decrypt(self, text, shift):
        return self.caesar_encrypt(text, -shift)

    def hypotenuse_calculator(self, a, b):
        try:
            a = float(a)
            b = float(b)
            result = ((a ** 2) + (b ** 2)) ** 0.5
            return f"The hypotenuse is: {result}"
        except ValueError:
            return "Invalid input. Please provide valid numbers."

    def rock_paper_scissors(self, user_choice):
        choices = ['rock', 'paper', 'scissors']
        if user_choice.lower() not in choices:
            return "Invalid choice. Please choose rock, paper, or scissors."
        
        computer_choice = random.choice(choices)
        user_choice = user_choice.lower()
        
        if computer_choice == user_choice:
            result = "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            result = "You win!"
        else:
            result = "You lose!"
        
        return f"{result}\nComputer chose: {computer_choice}\nYou chose: {user_choice}"

    def roll_dice(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        return f"You rolled: {dice1} + {dice2} = {total}"

    def lookup_acronym(self, acronym):
        acronym = acronym.upper()
        if acronym in self.acronym_dict:
            return f"{acronym}: {self.acronym_dict[acronym]}"
        else:
            return f"Sorry, '{acronym}' not found in the acronym dictionary."

    def check_divisible(self, x, y):
        try:
            x = int(x)
            y = int(y)
            if y == 0:
                return "You can't divide by 0"
            elif x % y == 0:
                return f"{x} is divisible by {y}"
            else:
                return f"{x} is not divisible by {y}"
        except ValueError:
            return "Invalid input. Please provide valid integers."

    def flip_coin(self):
        result = random.choice(['Heads', 'Tails'])
        return f"The coin landed on: {result}"

    def simple_calculator(self, expression):
        try:
            # Basic safety check - only allow numbers, operators, and parentheses
            allowed_chars = set('0123456789+-*/().**√ ')
            if not all(c in allowed_chars for c in expression):
                return "Invalid characters in expression"
            
            # Replace common symbols
            expression = expression.replace('^', '**')
            expression = expression.replace('√', 'math.sqrt')
            
            # Evaluate the expression
            result = eval(expression)
            calculation = f"{expression} = {result}"
            self.calculator_history.append(calculation)
            return f"Result: {result}"
        except Exception as e:
            return f"Error: Invalid expression - {str(e)}"

def chatbot_response(user_input):
    chatbot = ChatbotLogic()
    user_input = user_input.lower().strip()
    
    # Handle different commands
    if user_input == 'bye':
        return "Goodbye! Thanks for chatting with me!"
    
    elif 'hello' in user_input or 'hi' in user_input:
        return "Hello there! How can I help you today?"
    
    elif 'how are you' in user_input:
        return "I'm just a bot, but I'm doing fine! Thanks for asking!"
    
    elif 'name' in user_input:
        return "I'm a simple chatbot created in Python. You can call me ChatBot!"
    
    elif 'built' in user_input:
        return "I was built on June 25, 2025 and I run on Python, the fastest growing programming language in the world!"
    
    elif 'creator' in user_input:
        return "I was created by Nikhil! Unfortunately, I can't show you the turtle graphics in this web interface, but the creator made some beautiful star patterns and spelled out 'NIKHIL' using Python turtle graphics!"
    
    elif 'joke' in user_input:
        return "Why did Beethoven get rid of his chickens?\n\nAll they ever said was 'Bach, Bach, Bach!' 🐔🎵"
    
    elif user_input.startswith('hyp '):
        # Extract numbers from input like "hyp 3 4"
        parts = user_input.split()
        if len(parts) >= 3:
            return chatbot.hypotenuse_calculator(parts[1], parts[2])
        else:
            return "Please provide two numbers after 'hyp'. Example: 'hyp 3 4'"
    
    elif user_input.startswith('game '):
        # Extract choice from input like "game rock"
        parts = user_input.split()
        if len(parts) >= 2:
            return chatbot.rock_paper_scissors(parts[1])
        else:
            return "Please provide your choice after 'game'. Example: 'game rock'"
    
    elif user_input == 'roll':
        return chatbot.roll_dice()
    
    elif user_input.startswith('acronym '):
        # Extract acronym from input like "acronym API"
        parts = user_input.split()
        if len(parts) >= 2:
            return chatbot.lookup_acronym(parts[1])
        else:
            return "Please provide an acronym to look up. Example: 'acronym API'"
    
    elif user_input.startswith('divisible '):
        # Extract numbers from input like "divisible 10 2"
        parts = user_input.split()
        if len(parts) >= 3:
            return chatbot.check_divisible(parts[1], parts[2])
        else:
            return "Please provide two numbers after 'divisible'. Example: 'divisible 10 2'"
    
    elif user_input == 'coin':
        return chatbot.flip_coin()
    
    elif user_input.startswith('calc '):
        # Extract expression from input like "calc 2+2"
        expression = user_input[5:]  # Remove 'calc ' prefix
        return chatbot.simple_calculator(expression)
    
    elif user_input.startswith('cipher '):
        # Extract cipher command like "cipher encrypt hello 3" or "cipher decrypt khoor 3"
        parts = user_input.split()
        if len(parts) >= 4:
            operation = parts[1]
            text = parts[2]
            try:
                shift = int(parts[3])
                if operation == 'encrypt':
                    result = chatbot.caesar_encrypt(text, shift)
                    return f"Encrypted: {result}"
                elif operation == 'decrypt':
                    result = chatbot.caesar_decrypt(text, shift)
                    return f"Decrypted: {result}"
                else:
                    return "Use 'encrypt' or 'decrypt'. Example: 'cipher encrypt hello 3'"
            except ValueError:
                return "Shift must be a number. Example: 'cipher encrypt hello 3'"
        else:
            return "Format: 'cipher [encrypt/decrypt] [text] [shift]'. Example: 'cipher encrypt hello 3'"
    
    elif 'quiz' in user_input:
        return """Welcome to the Math Quiz! Here are 5 questions:

1. What is 20000 + 900010? (Answer: 920010)
2. What is 5 × 90? (Answer: 450)  
3. What is 100090 ÷ 10? (Answer: 10009)
4. What is 70 × 29? (Answer: 2030)
5. What is 7.934 × 4.794 rounded to the nearest tenth? (Answer: 38.0)

Try answering these questions and let me know your score!"""
    
    elif 'ttt' in user_input:
        return """Welcome to Tic-Tac-Toe! 

Unfortunately, I can't play interactive games in this web interface, but here's how you can play:

The board positions are numbered 1-9:
 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 

Players take turns choosing positions. First to get 3 in a row wins!
You can play this game with a friend using the original Python version."""
    
    elif 'help' in user_input:
        return """Here are the available commands:
        
• hi/hello - Say hello
• how are you - Ask how I'm doing  
• name - Get my name
• built - Learn when I was built
• creator - Learn about my creator
• joke - Get a joke
• hyp [num1] [num2] - Calculate hypotenuse (e.g., 'hyp 3 4')
• game [choice] - Play rock-paper-scissors (e.g., 'game rock')
• roll - Roll dice
• acronym [term] - Look up acronym (e.g., 'acronym API')
• divisible [num1] [num2] - Check divisibility (e.g., 'divisible 10 2')
• coin - Flip a coin
• calc [expression] - Calculate (e.g., 'calc 2+2*3')
• cipher [encrypt/decrypt] [text] [shift] - Caesar cipher (e.g., 'cipher encrypt hello 3')
• quiz - Take a math quiz
• ttt - Learn about tic-tac-toe
• bye - Say goodbye"""
    
    else:
        return "I don't understand that command. Try 'help' to see available commands, or use one of the specific formats like 'hyp 3 4' or 'game rock'."

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get('message', '')
        response = chatbot_response(user_input)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "Chatbot API is running"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)