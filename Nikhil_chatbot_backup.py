from turtle import *

def chatbot():




    print('\033[1;31mHi I am a simple ChatBot that can answer basic questions, play mini games, and perform calculations.')
    print('\033[1;31mHere are My inputs:')
    print('\033[1;31m---------------------------------------------------------------------------------------------')
    print('\033[1;35m---------------------------------------------------------------------------------------------')
    print('\033[1;36m---------------------------------------------------------------------------------------------')
    print('\033[1;36m1. hi: for asking hi')
    print('\033[1;36m2. bye: for exiting')
    print('\033[1;36m3. how are you doing: for asking how are you doing')
    print('\033[1;36m4. creator : for the name made in turtle of the creator of this project')
    print('\033[1;36m5. hyp: for a hypotenuse calculator')
    print('\033[1;36m6. name: for its name')
    print('\033[1;36m7. calc: to open a calculator')
    print('\033[1;36m8. joke: for a good joke')
    print('\033[1;36m9. game: for a simple rock-paper-scissors best out of 10')
    print('\033[1;36m10. built: for when this was built and what this runs on')
    print('\033[1;36m11. roll: for a dice rolling game against some one else')
    print('\033[1;36m12. acronym: to search a acronym dictionary for computer science acronyms')
    print('\033[1;36m13. divisible: for a divisibility calculater')
    print('\033[1;36m14. coin: for a coin flip simulator with a fair coin')
    print('\033[1;36m15. quiz: for a 5 question math quiz')
    print('\033[1;36m16. cipher: for a ceaser cipher encrypter and decrypter')
    print('\033[1;36m17. ttt: to play tic-tac-toe against another person')

    while True:
        user_input = input("\033[1;34mYou: ").lower()

        if user_input == 'bye':
            print("Bot: Goodbye!")
            break

        elif 'cipher' in user_input:

            def caesar_encrypt(text, shift):
                encrypted = ""
                for char in text:
                    if char.isalpha():
                        base = ord('A') if char.isupper() else ord('a')
                        encrypted += chr((ord(char) - base + shift) % 26 + base)
                    else:
                        encrypted += char
                return encrypted

            def caesar_decrypt(text, shift):
                return caesar_encrypt(text, -shift)

            def main():
                print("\033[1;31m=== Caesar Cipher Tool ===")
                mode = input("\033[1;31mDo you want to encrypt or decrypt? (e/d): ").lower()

                if mode not in ['e', 'd']:
                    print("Invalid option. Choose 'e' for encrypt or 'd' for decrypt.")
                    return

                message = input("Enter your message: ")
                try:
                    shift = int(input("Enter the shift amount (e.g., 3): "))
                except ValueError:
                    print("Shift must be a number.")
                    return

                if mode == 'e':
                    result = caesar_encrypt(message, shift)
                    print("Encrypted message:", result)
                else:
                    result = caesar_decrypt(message, shift)
                    print("Decrypted message:", result)

            if __name__ == "__main__":
                main()

        elif 'hyp' in user_input:
            def get_float(prompt):
                while True:
                    try:
                        return float(input(prompt))
                    except ValueError:
                        print("That's not a valid number. Try again.")

            def hyp():
                a = get_float('What is the first length?\n')
                b = get_float('What is the second length?\n')
                print('The hypotenuse is:', ((a ** 2) + (b ** 2)) ** 0.5)
            hyp()




        elif 'hello' in user_input or 'hi' in user_input:
            print("\033[1;31mBot: Hello there!")

        elif 'how are you' in user_input:
            print("\033[1;31mBot: I'm just a bot, but I'm doing fine!")
        elif 'creator' in user_input:

            euler = Turtle()
            euler.shape('turtle')
            sherva = Turtle()
            sherva.shape("turtle")
            sherva.pensize(20)
            euler.pensize(20)

            def main():
                sherva.color('blue', 'yellow')
                sherva.begin_fill()
                euler.color('blue', 'yellow')
                euler.begin_fill()

                def euler_drwing(turtle):
                    euler.penup()
                    euler.backward(800)
                    euler.pendown()
                    for i in range(5):
                        euler.left(144)
                        euler.forward(50)
                    euler.penup()
                    euler.forward(100)
                    euler.pendown()

                    for i in range(5):
                        euler.left(144)
                        euler.forward(50)
                    euler.penup()
                    euler.forward(100)
                    euler.pendown()
                    for i in range(5):
                        euler.left(144)
                        euler.forward(50)
                    euler.penup()
                    euler.forward(50)
                    euler.pendown()
                    for i in range(5):
                        euler.left(144)
                        euler.forward(50)
                    euler.penup()
                    euler.forward(100)
                    euler.pendown()
                    for i in range(5):
                        euler.left(144)
                        euler.forward(50)
                    euler.penup()
                    euler.forward(100)
                    euler.pendown()
                    for i in range(5):
                        euler.left(144)
                        euler.forward(50)
                    euler.penup()
                    euler.forward(100)
                    euler.pendown()

                def letter_N(turtle):
                    sherva.backward(200)
                    sherva.clear()
                    sherva.left(90)
                    sherva.forward(100)
                    sherva.right(150)
                    sherva.forward(110)
                    sherva.left(150)
                    sherva.forward(100)
                    sherva.up()
                    # next letter
                    sherva.right(90)
                    sherva.forward(50)
                    sherva.down()

                def letter_I(turtle):
                    sherva.forward(100)
                    sherva.backward(50)
                    sherva.right(90)
                    sherva.forward(100)
                    sherva.left(90)
                    sherva.backward(50)
                    sherva.forward(100)
                    sherva.up()
                    sherva.forward(50)
                    sherva.down()

                def letter_K(turtle):
                    sherva.left(90)
                    sherva.forward(100)
                    sherva.backward(50)
                    sherva.right(45)
                    sherva.forward(75)
                    sherva.backward(75)
                    sherva.right(90)
                    sherva.forward(75)
                    sherva.left(45)
                    sherva.up()
                    sherva.forward(50)
                    sherva.down()

                def letter_H(turtle):
                    sherva.left(90)
                    sherva.forward(100)
                    sherva.backward(50)
                    sherva.right(90)
                    sherva.forward(50)
                    sherva.left(90)
                    sherva.forward(50)
                    sherva.backward(100)
                    #
                    sherva.up()
                    sherva.right(90)
                    sherva.forward(50)
                    sherva.left(90)
                    sherva.forward(100)
                    sherva.right(90)
                    sherva.down()
                    #

                def letter_i(turtle):
                    sherva.forward(100)
                    sherva.backward(50)
                    sherva.right(90)
                    sherva.forward(100)
                    sherva.left(90)
                    sherva.backward(50)
                    sherva.forward(100)
                    sherva.up()
                    sherva.forward(50)
                    sherva.left(90)
                    sherva.down()

                def letter_L(turtle):
                    sherva.forward(100)
                    sherva.backward(100)
                    sherva.right(90)
                    sherva.forward(75)
                    sherva.up()
                    sherva.right(90)
                    sherva.forward(200)
                    sherva.down()

                sherva.end_fill()

                def shapes(turtle):
                    sherva.color('blue', 'red')
                    sherva.begin_fill()
                    for i in range(5):
                        sherva.left(144)
                        sherva.forward(50)
                    sherva.up()
                    sherva.forward(75)
                    sherva.down()
                    for i in range(4):
                        sherva.forward(50)
                        sherva.right(90)
                        sherva.up()
                    sherva.forward(75)
                    sherva.down()
                    for i in range(3):
                        sherva.forward(50)
                        sherva.left(120)
                    sherva.end_fill()
                    sherva.up()
                    sherva.right(90)
                    sherva.forward(400)
                    sherva.down()
                    for i in range(5):
                        sherva.left(144)
                        sherva.forward(50)
                    sherva.up()
                    sherva.right(90)
                    sherva.forward(200)
                    sherva.down()
                    sherva.circle(30)
                    sherva.right(90)
                    sherva.forward(100)
                    sherva.right(90)
                    sherva.forward(50)
                    sherva.backward(50)
                    sherva.left(90)
                    sherva.forward(40)
                    sherva.right(90)
                    sherva.forward(50)
                    sherva.penup()
                    sherva.right(90)
                    sherva.forward(100)
                    sherva.pendown()

                euler_drwing(euler)
                letter_N(sherva)
                letter_I(sherva)
                letter_K(sherva)
                letter_H(sherva)
                letter_i(sherva)
                letter_L(sherva)
                shapes(sherva)

            main()


        elif 'name' in user_input:
            print("\033[1;31mBot: I'm a simple chatbot created in Python.")

        elif 'calc' in user_input:
            print ('\033[1;31mopening calculator..............')
            import math

            class Calculator:
                def __init__(self):
                    self.history = []

                def add(self, a, b):
                    result = a + b
                    self.history.append(f"{a} + {b} = {result}")
                    return result

                def subtract(self, a, b):
                    result = a - b
                    self.history.append(f"{a} - {b} = {result}")
                    return result

                def multiply(self, a, b):
                    result = a * b
                    self.history.append(f"{a} * {b} = {result}")
                    return result

                def divide(self, a, b):
                    if b == 0:
                        raise ValueError("Cannot divide by zero!")
                    result = a / b
                    self.history.append(f"{a} / {b} = {result}")
                    return result

                def power(self, a, b):
                    result = a ** b
                    self.history.append(f"{a} ^ {b} = {result}")
                    return result

                def square_root(self, a):
                    if a < 0:
                        raise ValueError("Cannot calculate square root of negative number!")
                    result = math.sqrt(a)
                    self.history.append(f"√{a} = {result}")
                    return result

                def percentage(self, a, b):
                    result = (a / 100) * b
                    self.history.append(f"{a}% of {b} = {result}")
                    return result

                def clear_history(self):
                    self.history = []
                    print("History cleared!")

                def show_history(self):
                    if not self.history:
                        print("No calculations in history.")
                    else:
                        print("\n--- Calculation History ---")
                        for calc in self.history:
                            print(calc)

                def evaluate_expression(self, expression):
                    """Safely evaluate mathematical expressions"""
                    try:
                        # Replace common symbols
                        expression = expression.replace('^', '**')
                        expression = expression.replace('√', 'math.sqrt')

                        # Only allow safe operations
                        allowed_chars = set('0123456789+-*/().** ')
                        allowed_functions = {'math.sqrt', 'math.sin', 'math.cos', 'math.tan', 'math.log'}

                        # Basic safety check
                        if any(char.isalpha() and 'math.' not in expression for char in expression):
                            if not any(func in expression for func in allowed_functions):
                                raise ValueError("Invalid expression")

                        result = eval(expression)
                        self.history.append(f"{expression} = {result}")
                        return result
                    except Exception as e:
                        raise ValueError(f"Invalid expression: {e}")

            def main():
                calc = Calculator()

                print("\033[1;31m=== Python Calculator ===")
                print("\033[1;31mAvailable operations:")
                print("\033[1;31m1. Basic arithmetic (+, -, *, /)")
                print("\033[1;31m2. Power (^)")
                print("\033[1;31m3. Square root (sqrt)")
                print("\033[1;31m4. Percentage (%)")
                print("\033[1;31m5. Expression evaluation")
                print("\nCommands:")
                print("\033[1;31m- 'history' - Show calculation history")
                print("\033[1;31m- 'clear' - Clear history")
                print("\033[1;31m- 'quit' or 'exit' - Exit calculator")
                print("\033[1;31m-" * 40)

                while True:
                    try:
                        user_input = input("\nEnter calculation or command: ").strip().lower()

                        if user_input in ['quit', 'exit', 'q']:
                            print("Thanks for using the calculator!")
                            break

                        elif user_input == 'history':
                            calc.show_history()
                            continue

                        elif user_input == 'clear':
                            calc.clear_history()
                            continue

                        elif user_input == '':
                            continue

                        # Handle different input formats
                        if '+' in user_input:
                            parts = user_input.split('+')
                            if len(parts) == 2:
                                a, b = float(parts[0].strip()), float(parts[1].strip())
                                result = calc.add(a, b)
                                print(f"Result: {result}")
                                continue

                        elif '-' in user_input and user_input.count('-') == 1:
                            parts = user_input.split('-')
                            if len(parts) == 2 and parts[0].strip():
                                a, b = float(parts[0].strip()), float(parts[1].strip())
                                result = calc.subtract(a, b)
                                print(f"Result: {result}")
                                continue

                        elif '*' in user_input:
                            parts = user_input.split('*')
                            if len(parts) == 2:
                                a, b = float(parts[0].strip()), float(parts[1].strip())
                                result = calc.multiply(a, b)
                                print(f"Result: {result}")
                                continue

                        elif '/' in user_input:
                            parts = user_input.split('/')
                            if len(parts) == 2:
                                a, b = float(parts[0].strip()), float(parts[1].strip())
                                result = calc.divide(a, b)
                                print(f"Result: {result}")
                                continue


                        elif user_input.startswith('sqrt'):
                            num_str = user_input.replace('sqrt', '').strip('() ')
                            if num_str:
                                num = float(num_str)
                                result = calc.square_root(num)
                                print(f"Result: {result}")
                                continue


                        elif '^' in user_input or '**' in user_input:
                            if '^' in user_input:
                                parts = user_input.split('^')
                            else:
                                parts = user_input.split('**')
                            if len(parts) == 2:
                                a, b = float(parts[0].strip()), float(parts[1].strip())
                                result = calc.power(a, b)
                                print(f"Result: {result}")
                                continue

                        # Try to evaluate as expression
                        try:
                            result = calc.evaluate_expression(user_input)
                            print(f"Result: {result}")
                        except ValueError as e:
                            print(f"Error: {e}")
                            print("Please enter a valid calculation or command.")

                    except ValueError as e:
                        print(f"Error: {e}")
                    except KeyboardInterrupt:
                        print("\nGoodbye!")
                        break
                    except Exception as e:
                        print(f"An error occurred: {e}")

            if __name__ == "__main__":
                main()
        elif 'joke' in user_input:
            print('\033[1;31mBot: Why did Beethoven get rid of his chickens?')
            joke = input('\033[1;32mYou: ').lower()
            if joke == 'you: all they ever said was, “bach, bach, bach!”':
                print('you got it, good job!!! :)')
            else:
                print ('\033[1;31mBot: No the answer was: All they ever said was, “Bach, Bach, Bach!” :)')
        elif 'game' in user_input:
            print('\033[1;31mentering rock-paper-scissors...... ')
            import random
            my_list=['rock','paper','scissors']
            weights=[5,5,5]

            for i in range (0,10):
                computer_choice_list=random.choices(my_list, weights=weights, k=1)
                computer_choice=computer_choice_list[0]
                user_choice=input('D\033[1;31mo you want to choose rock paper or scissors?\n')

                if user_choice not in my_list:
                    print('invalid input')
                if computer_choice==user_choice:
                    print('Its a tie')
                elif user_choice == 'rock' and computer_choice == 'scissors':
                    print('win')
                elif user_choice == 'paper' and computer_choice == 'rock':
                    print('win')
                elif user_choice == 'scissors' and computer_choice == 'paper':
                    print('win')
                else: print('you lose')
                print('Computer Choice: ', computer_choice)
                print('My Choice: ', user_choice)


        elif 'built' in user_input:
            print('\033[1;31mI was built on june-25-2025 and I run on Python, the fastest growing programing language in the world!')
        elif 'roll' in user_input:
            print('\033[1;31mentering dice game-------------')
            import random
            def roll_dice():
                dice_total = random.randint(1,6)+random.randint(1,6)
                return dice_total
            def center():
                player1 = input("\033[1;31mEnter player one's name-- ")
                player2 = input("\033[1;31mEnter player two's name-- ")
                roll1 = roll_dice()
                roll2 = roll_dice()
                print(player1,'rolled a', roll1)
                print(player2, 'rolled a', roll2)
                if roll1>roll2:
                    print(player1, 'wins')
                elif roll1==roll2:
                    print('its a tie')
                else:
                      print(player2, 'wins')
            roll_dice()
            center()
        elif 'acronym' in user_input:
            # Dictionary of acronyms
            acronym_dict = {
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

            # User input loop
            while True:
                user_input = input("\033[1;31mEnter an acronym to look up (or type 'exit' to quit): ").upper()

                if user_input == "EXIT":
                    print("Goodbye!")
                    break
                elif user_input in acronym_dict:
                    print(f"{user_input}: {acronym_dict[user_input]}")
                else:
                    print(f"Sorry, '{user_input}' not found in the acronym dictionary.")
        elif 'divisible' in user_input:
            def divisible():
                x = int(input('\033[1;31mwhat is the first number?\n'))
                y = int(input('\033[1;31mwhat is the second number\n'))
                if y or x  == 0:
                    print('you cant divide by 0')
                elif x % y != 0:
                    print('the numbers are not divisible')
                elif x % y == 0:
                    print('the numbers are divisible')

                else:
                    print('Error!!!!!!!')
            divisible()
        elif 'coin' in user_input:
            import random
            def flip():
                print ('\033[1;31mWelcome to the coin toss simulator, here the coin is fair unlike a real coin.')
                ques = input('\033[1;31mdo you want to flip or quit,(type flip for flip and quit for quit)\n').lower()
                if ques == 'flip':
                    print('flipping')
                    flip = random.randint(1,2)
                    if flip == 1:
                        print ('It landed on Heads')
                    else:
                        print('It landed on Tails')
                else: print ('exiting')
            flip()


        elif 'quiz' in user_input:
            score=0
            x1 = int(input('what is 20000+900010\n'))
            #if x1 == int:
            if x1 == 920010:
                print('correct')
                score = score+1
            else: print ('\033[1;31mwrong, the answer was 920010')
            #else:
                #print('error')

            x2 = int(input('what is 5 x 90\n'))
            #if x2 == int:
            if x2 == 450:
                print ('correct')
                score = score+1
            else: print ('\033[1;31mwrong, the answer was 450')
            #else:
                #print('error')

            x3 = int(input('what is 100090/10\n'))
            #if x3 == int:
            if x3 == 10009:
                print('correct')
                score = score+1
            else:
                print('\033[1;31mwrong, the answer was 10009')
            #else: print('error')
            x4 = int(input('what is 70 x 29\n'))
            #if x4 == int:

            if x4 == 2030:
                print('correct')
                score = score+1
            else:
                print('\033[1;31mwrong, the answer was 2030')
            #else:print('error')
            x5 = float(input('what is 7.934 x 4.794 (round to the nearest tenth)\n'))
            #if x5 == int:

            if x5 == 38.0:
                print('correct')
                score=score+1
            else:
                print('\033[1;31mwrong, the answer was 38.0')
            print ("Your final score was:", score, "/ 5")
            #else: print('error')
        elif 'ttt' in user_input:
            print ('entering tic-tac-toe')

            def print_board(board):
                """Prints the Tic-Tac-Toe board."""
                print("-------------")
                for i in range(3):
                    print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
                    print("-------------")

            def player_input(board, player):
                """Gets the player's move and updates the board."""
                while True:
                    try:
                        move = int(input(f"Player {player}, enter your move (1-9): "))
                        if 1 <= move <= 9 and board[move - 1] == " ":
                            board[move - 1] = player
                            break
                        else:
                            print("Invalid move. Try again.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

            def check_win(board, player):
                """Checks if the given player has won the game."""
                win_combinations = [
                    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
                    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
                    [0, 4, 8], [2, 4, 6]  # diagonals
                ]
                for combo in win_combinations:
                    if all(board[i] == player for i in combo):
                        return True
                return False

            def check_tie(board):
                """Checks if the game is a tie."""
                return " " not in board

            def play_game():
                """Main function to run the Tic-Tac-Toe game."""
                board = [" "] * 9
                current_player = "X"
                game_over = False

                while not game_over:
                    print_board(board)
                    player_input(board, current_player)

                    if check_win(board, current_player):
                        print_board(board)
                        print(f"Player {current_player} wins!")
                        game_over = True
                    elif check_tie(board):
                        print_board(board)
                        print("It's a tie!")
                        game_over = True
                    else:
                        current_player = "O" if current_player == "X" else "X"

                print("Game Over")

            # Start the game
            play_game()
        

        else:
            print("\033[1;31mBot: I don't understand that yet.")
        

# chatbot()