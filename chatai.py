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
    print('\033[1;36m18. ai: to play tic-tac-toe against an ai that learns from past games and eventually never loses')

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
        elif ('ai') in user_input:
                    '''
        This is a reinforcement learning AI that learns to play the game of TicTacToe by
        ...playing against random opponents - and you!

        I've coded so that it doesn't require understanding any advanced coding techniques.
        (I don't use classes, list comprehensions, slicing, recursion, exceptions, etc.)
        (Understanding the code fully generally requires understanding variables,
        ...functions, lists, dictionaries, loops, and basic format strings.)

        In this code, a TicTacToe game is represented by a list of 9 values.
        For example, the board

        OXO
        -OX
        XOX

        is represented in the code with
        ["opp", "ai", "opp", "empty", "opp", "ai", "ai", "opp", "ai"]

        I go from right-to-left, top-to-bottom (just like reading).
        ("opp" is short for "opponent")

        Then, the AI stores a dictionary of all the game boards its ever seen.
        Each game board has its own dictionary of moves that the AI has made in that scenario.
        Then, each move is given a score of how good it is for the AI.

        All moves start out with a DEFAULT_SCORE of 0.
        If a move is definitely a win, the score should be closer to a WIN_SCORE of 5.
        If it's definitely a loss, it should be closer to a LOSE_SCORE of -15.
        If the move definitely leads to a tie, it should be closer to a TIE_SCORE of 1.
        (Feel free to play around with these numbers!)

        When the AI needs to make a move, it tries all of the moves!
        It plays 3 (FAKE_GAME_AMOUNT) completely random games for each of the moves it tries.
        Then, it updates the move scores based on how those games turned out.
        (This practice is called Monte Carlo estimation: you try stuff randomly and see how it turns out.)

        Move scores are updated using the following rule:
        NEW_MOVE_SCORE = OLD_MOVE_SCORE + (GAME_SCORE - OLD_MOVE_SCORE) * UPDATE_AMOUNT
        UPDATE_AMOUNT = GAME_FACTOR * DISCOUNT_FACTOR
        DISCOUNT_FACTOR = (DISTANCE_DISCOUNT ** (DISTANCE_FROM_END))
        (If this seems overwhelming, jump to the Explanation section below)

        GAME_SCORE
        The outcome of the game: either WIN_SCORE, TIE_SCORE, or LOSE_SCORE.

        UPDATE_AMOUNT
        A number between 0 and 1.
        How much we want to update the score to match the new score we saw.
        For example if UPDATE_AMOUNT is 0.5, then we'll change the NEW_MOVE_SCORE to be halfway between the OLD_MOVE_SCORE and the GAME_SCORE.

        GAME_FACTOR
        Usually around 0.5
        Set based on who the AI is playing.
        It will be higher when playing against humans so that it updates scores more from those games.

        DISTANCE_DISCOUNT
        Between 0 and 1
        Makes it so that moves early on in the game aren't updated as much
        ...because we're not actually certain that early moves cause the late-game outcomes.
        (It could be that bad moves were made late in the game.)
        For example, if your first move is in the center, but you lose the game,
        ...that doesn't mean that the first move was actually bad.
        The bigger this is, the more early moves are affected by later losses.

        DISTANCE_FROM_END
        A whole number between 1 and 5.
        How many moves away the move is from the last move of the game.
        It will be higher when moves are early on in the game, and 1 if it's the last move of the game.
        (This only counts moves from the perspective of the AI; the fastest possible game is 3 moves, the longest is 5.)

        Explanation:
        This equation for updating the scores is known as a Bellman Update equation,
        ...and is the main equation used in reinforcement learning!
        Hopefully it's explained in a way here that doesn't make it too scary!

        Basically, you take the old score and try to move it closer to the score you got for the game.
        But since you want to learn less from playing bad opponents, and you also aren't certain that you played the best,
        ...you don't want to set the score for the move to just be the outcome of the game.
        So, you shrink how much you change the score based on who you're playing
        ...and how many moves the move was from the end of the game.
        Moves closer to the end of the game were probably more responsible for losing the game, so they get updated more.
        Learning from better opponents is probably better, so you update moves more when playing against good opponents.

        Then, after playing these random games and updating the scores, it picks a move.
        It has a small chance to pick a non-optimal move so that it learns more about other scenarios.
        If it picks an optimal move, we say it's "exploiting", and if it picks a non-optimal move, we say it's "exploring".

        Finally, when the game is over, it saves what it learned so it can use that info for the next game!

        With that said, here's the code! Enjoy! :)
        '''

        # for saving and loading what the AI has learned
        import pickle
        # for checking to make sure files exist
        import os
        # for generating random numbers
        import random

        # where the AI's knowledge is stored
        SAVE_FILE = "knowledge.pkl"
        # How many games the AI should train playing against a random player before playing against a human
        # The higher the amount, the smarter the AI will seem to be
        PRACTICE_GAME_AMOUNT = 100
        # should the AI always make what it thinks is the best move?
        # True if it should make the best move
        # False if you want it to explore and learn more
        ALWAYS_EXPLOIT = True
        # if not always exploiting (ALWAYS_EXPLOIT is False)
        # ...this is the chance it will explore a non-optimal move
        EXPLORE_CHANCE = 0.2
        # before making a move, the AI tries each move and sees how that move does against a random player
        # how many games should it play against that random player in order to figure out what move is the best?
        # more games will make it seem more intelligent, but take longer to move
        FAKE_GAME_AMOUNT = 20
        # how much to weight games that are played against humans
        HUMAN_GAME_FACTOR = 1.0
        # how much to weight games that are played against the (random) AI
        REAL_AI_GAME_FACTOR = 0.5
        # how much to weight games that are played randomly against the random AI when testing moves
        # this should be very low because playing games randomly has little bearing
        # ...on how good the move is when played with strategy
        FAKE_GAME_FACTOR = 0.001
        # how much less to update the score of a move that happened early on in a game
        # this will be multiplied per move from the last move
        # for example, if this is 1/2, then the first move of a 3-move game (the shortest possible game) would only be updated by 1/8 the amount as the last move
        # (note that the score of a move is how good the AI thinks the move is)
        DISTANCE_DISCOUNT = 0.9

        # what should the score of a move that leads to a win be?
        WIN_SCORE = 5
        # what should the score of a move that leads to a loss be?
        LOSE_SCORE = -15
        # what should the score of a move that leads to a tie be?
        TIE_SCORE = 1
        # What should the score of a move that we have no data on be?
        DEFAULT_SCORE = 0

        # print information helpful for debugging and seeing the AIs decisions
        DEBUG = False

        # constants that I use in the code so I don't accidentally mistype the things they refer to
        HUMAN_OPPONENT = "human opponent"
        AI_OPPONENT = "ai opponent"
        AI_PLAYER = "ai"
        OPPONENT_PLAYER = "opp"
        NOT_OVER = "not over"
        TIE = "tie"
        EMPTY = "empty"


        # create the data structure that we'll save later
        # format: {scenario: {move: score, ...}, ...}
        # move_scores[scenario][move1] gives the score for making that move in that scenario
        move_scores = {}

        # check if the save file exists
        if os.path.isfile(SAVE_FILE):
            # replace the empty data with the saved data
            with open(SAVE_FILE, "rb") as save_file: # open the file
                move_scores = pickle.load(save_file) # load the data into the variable


        # ******* See the bottom of the file to understand what's actually being run ********

        # remember that a game is a list of 9 values like
        # ["opp", "ai", "opp", "empty", "opp", "ai", "ai", "opp", "ai"]

        def player_to_string(player):
            # convert the strings like "ai", "opp", and "empty" into "X", "O", and "-"
            if player == AI_PLAYER:
                return "X"
            elif player == OPPONENT_PLAYER:
                return "O"
            else:
                return "-"

        def display_game(game):
            # turn the player strings like "ai" and "opp" into displayable X's and O's
            strings = []
            for i in range(len(game)):
                strings.append(player_to_string(game[i]))
            # print the board
            print(strings[0] + strings[1] + strings[2])
            print(strings[3] + strings[4] + strings[5])
            print(strings[6] + strings[7] + strings[8])

        def make_move(game, space, player):
            game[space] = player
            return game

        def check_winner(game):
            for player in [AI_PLAYER, OPPONENT_PLAYER]:
                # check rows
                if game[0] == player and game[1] == player and game[2] == player:
                    return player
                if game[3] == player and game[4] == player and game[5] == player:
                    return player
                if game[6] == player and game[7] == player and game[8] == player:
                    return player
                # check columns
                if game[0] == player and game[3] == player and game[6] == player:
                    return player
                if game[1] == player and game[4] == player and game[7] == player:
                    return player
                if game[2] == player and game[5] == player and game[8] == player:
                    return player
                # check diagonals
                if game[0] == player and game[4] == player and game[8] == player:
                    return player
                if game[2] == player and game[4] == player and game[6] == player:
                    return player
            possible_moves = get_possible_moves(game)
            # determine if it's a tie or if the game is still in progress
            if len(possible_moves) == 0:
                return TIE
            else:
                return NOT_OVER

        def winner_to_game_score(winner):
            # returns the game score, given a winner of the game
            if winner == AI_PLAYER:
                game_score = WIN_SCORE
            elif winner == OPPONENT_PLAYER:
                game_score = LOSE_SCORE
            else:
                game_score = TIE_SCORE
            return game_score

        # a scenario is an unmodifiable game (turn the modifiable list into an unmodifiable tuple)
        # (this is done because lists can't be keys in dictionaries, but tuples can be)
        def game_to_scenario(game):
            return tuple(game)

        # this is the heart of the AI's learning
        # given data about what moves were made in what scenarios and what score those moves lead to, update the AI to make better choices
        def update_from_data(data, game_factor, game_score):
            # data is in the format [[scenario, move], ...]
            # it's a sequence of moves that were made in the game
            # game_factor and game_score are described in the Bellman equation at the top of the file

            number_of_moves = len(data)
            for index in range(number_of_moves):
                datapoint = data[index]
                scenario = datapoint[0]
                move = datapoint[1]

                # make sure that the storage slot for the data exists; create it if it doesn't
                if scenario not in move_scores.keys():
                    move_scores[scenario] = {}
                if move not in move_scores[scenario].keys():
                    move_scores[scenario][move] = DEFAULT_SCORE

                old_move_score = move_scores[scenario][move]

                # compute Bellman's equation - described in the comment at the top of the file
                distance_from_end = number_of_moves - index
                discount_factor = DISTANCE_DISCOUNT ** distance_from_end
                update_amount = game_factor * discount_factor
                new_move_score = old_move_score + (game_score - old_move_score) * update_amount

                # store the updated score
                move_scores[scenario][move] = new_move_score

        def copy_list(given_list):
            new_list = []
            for thing in given_list:
                new_list.append(thing)
            return new_list

        def get_possible_moves(game):
            # get the indexes of the empty spaces in the board
            possible_moves = []
            for i in range(len(game)):
                if game[i] == EMPTY:
                    possible_moves.append(i)
            return possible_moves

        def train_ai(opponent):
            # game of Tic Tac Toe with all nine slots empty
            game = [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
            who_goes_first = random.choice([OPPONENT_PLAYER, AI_PLAYER])
            is_game_over = False
            whose_turn = who_goes_first
            # format: [[scenario, move], ...]
            game_data = []
            # there's no winner yet
            winner = None

            while is_game_over is False:
                if opponent == HUMAN_OPPONENT:
                    print("Current game state:")
                    display_game(game)
                if whose_turn == AI_PLAYER:
                    # try each move and learn from them
                    learn_from_simulation(game)

                    # randomly decide whether to explore or exploit
                    if ALWAYS_EXPLOIT == True:
                        random_explore_number = 1
                    else:
                        # get a random decimal number between 0 and 1
                        random_explore_number = random.random()
                    if random_explore_number <= EXPLORE_CHANCE:
                        # explore
                        # pick a move at random
                        if opponent == HUMAN_OPPONENT:
                            print("Exploring to see what happens...")
                        possible_moves = get_possible_moves(game)
                        move = random.choice(possible_moves)
                    else:
                        # exploit
                        # pick the move that has the highest score
                        if opponent == HUMAN_OPPONENT:
                            print("Choosing the best move...")
                        # start the highest score at negative infinity
                        highest_score = float('-inf')
                        move = None
                        possible_moves = get_possible_moves(game)
                        for possible_move in possible_moves:
                            # these will all exist because it will have tried all of these moves during the simulation
                            # (that is, no need to check if they're empty / nonexistent)
                            scenario = game_to_scenario(game)
                            game_score = move_scores[scenario][possible_move]
                            if game_score > highest_score:
                                # this is the highest scoring move so far - save it!
                                move = possible_move
                                highest_score = game_score

                    # save the game as a scenario before it gets modified by the move
                    scenario = game_to_scenario(game)
                    if DEBUG and opponent == HUMAN_OPPONENT:
                        print("How the AI views the moves:")
                        human_understandable_move_scores = {}
                        for debug_move in move_scores[scenario].keys():
                            human_understandable_move_scores[debug_move + 1] = move_scores[scenario][debug_move]
                        print(human_understandable_move_scores)
                    game_data.append([scenario, move])
                    game = make_move(game, move, AI_PLAYER)
                    if opponent == HUMAN_OPPONENT:
                        print(f"The AI played move {move + 1}.")
                    whose_turn = OPPONENT_PLAYER
                else:
                    # opponent's turn
                    if opponent == HUMAN_OPPONENT:
                        # get the move from the user
                        move = get_move_from_user(game)
                    else:
                        # get a random move
                        possible_moves = get_possible_moves(game)
                        move = random.choice(possible_moves)
                    game = make_move(game, move, OPPONENT_PLAYER)
                    whose_turn = AI_PLAYER

                # determine if the game is over
                winner = check_winner(game)
                if winner is not NOT_OVER:
                    is_game_over = True

            if opponent == HUMAN_OPPONENT:
                if winner == TIE:
                    print("Tie game!")
                else:
                    print(f"The winner is {player_to_string(winner)}!")
                display_game(game)

            # tell the AI how well it did
            game_score = winner_to_game_score(winner)

            # set how much we want the results to influence what the AI learns
            if opponent == AI_PLAYER:
                game_factor = REAL_AI_GAME_FACTOR
            else:
                # opponent == OPPONENT_PLAYER:
                game_factor = HUMAN_GAME_FACTOR

            # update the scores of the moves that were played
            update_from_data(game_data, game_factor, game_score)

        def get_move_from_user(game):
            # get the move from the user
            print("Enter a number between 1 and 9 (1 is top left, 9 is bottom right, 5 is middle):")
            # convert human numbers (starting at 1) into indexes (starting at 0)
            move = int(input()) - 1
            while move not in get_possible_moves(game):
                print("Invalid move. Try again:")
                move = int(input()) - 1
            return move

        def learn_from_simulation(game):
            # try each possible move a certain number of times and
            # see how well that move (plus other random moves) does against a random opponent
            # Update the scores accordingly
            # there will always be moves available because the game is not over
            possible_moves = get_possible_moves(game)
            scenario = copy_list(game)
            for move in possible_moves:
                game_data = []
                # create a copy of the game that the simulations can happen on
                simulation_game = copy_list(game)
                scenario = game_to_scenario(simulation_game)
                game_data.append([scenario, move])
                simulation_game = make_move(simulation_game, move, AI_PLAYER)
                for i in range(FAKE_GAME_AMOUNT):
                    copied_simulation_game = copy_list(simulation_game)
                    copied_game_data = copy_list(game_data)
                    play_random_and_update(copied_simulation_game, copied_game_data)

        def play_random_and_update(copied_simulation_game, copied_game_data):
            whose_turn = OPPONENT_PLAYER
            # while the game is not over, make random moves
            while check_winner(copied_simulation_game) == NOT_OVER:
                # turn the game into a scenario before the move is made so we can save the scenario if needed later
                scenario = game_to_scenario(copied_simulation_game)

                # make a random move for the current player
                possible_moves = get_possible_moves(copied_simulation_game)
                move = random.choice(possible_moves)
                copied_simulation_game = make_move(copied_simulation_game, move, whose_turn)

                if whose_turn == AI_PLAYER:
                    # if the move was made by the AI, save it so we can update the score of the move
                    # ...based on how the game goes
                    copied_game_data.append([scenario, move])
                    whose_turn = OPPONENT_PLAYER
                else:
                    whose_turn = AI_PLAYER

            # set the score based on the outcome of the game
            winner = check_winner(copied_simulation_game)
            game_score = winner_to_game_score(winner)
            # these are fake random games the AI is playing, so we use the appropriate scaling (FAKE_GAME_FACTOR)
            update_from_data(copied_game_data, FAKE_GAME_FACTOR, game_score)

        # *******The code is actually run here********
        # you can also have it play against an AI_OPPONENT

        # allow it to explore during training, but save what the user wanted
        exploit_against_human = ALWAYS_EXPLOIT
        ALWAYS_EXPLOIT = False
        print("Training against a random opponent...")
        for game_index in range(PRACTICE_GAME_AMOUNT):
            percent_complete = game_index / PRACTICE_GAME_AMOUNT * 100
            # round the percentage one decimal place
            percent_complete = round(percent_complete, 1)
            print(f"Training is {percent_complete}% complete...")
            train_ai(AI_OPPONENT)

        print("Training complete! Saving what I learned...")

        with open(SAVE_FILE, "wb") as save_file:
            pickle.dump(move_scores, save_file)

        # set the ALWAYS_EXPLOIT variable back to what it was
        ALWAYS_EXPLOIT = exploit_against_human

        print("Data saved - I'm ready to play!")

        while True:
            # continually play against the human and learn from the games
            print("New Game!")
            train_ai(HUMAN_OPPONENT)

            # save the training data
            with open(SAVE_FILE, "wb") as save_file:
                pickle.dump(move_scores, save_file)    

        else:
            print("\033[1;31mBot: I don't understand that yet.")
        

chatbot()