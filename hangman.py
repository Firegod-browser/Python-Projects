import random


def choose_word():
    words = ['python', 'developer', 'hangman', 'challenge', 'programming', 'code', 'function']
    return random.choice(words).lower()


def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |    
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |    
           |
        """
    ]
    return stages[tries]


def play():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print("Let's play Hangman!")

    while tries > 0 and word_letters:
        print(display_hangman(tries))
        print("Word: " + " ".join([letter if letter in guessed_letters else "_" for letter in word]))
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
            print(f"Good guess! {guess} is in the word.")
        else:
            guessed_letters.add(guess)
            tries -= 1
            print(f"Sorry, {guess} is not in the word. Tries left: {tries}")

    if not word_letters:
        print(display_hangman(tries))
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(display_hangman(tries))
        print(f"Game Over! The word was: {word}")


if __name__ == "__main__":
    play()
