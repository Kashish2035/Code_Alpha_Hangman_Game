import random
import sys

WORDS = [
    "python", "hangman", "computer", "challenge", "programming",
    "developer", "stream", "algorithm", "function", "variable"
]

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    ======="""
]

MAX_WRONG = len(HANGMAN_PICS) - 1

def choose_word():
    return random.choice(WORDS)

def display_state(secret_word, guessed_letters, wrong_guesses):
    # Display hangman picture
    print(HANGMAN_PICS[wrong_guesses])
    # Display word with underscores for unguessed letters
    display = " ".join([c if c in guessed_letters else "_" for c in secret_word])
    print("\nWord: ", display)
    print(f"\nGuessed letters: {', '.join(sorted(guessed_letters))}")
    print(f"Wrong guesses left: {MAX_WRONG - wrong_guesses}\n")

def get_guess(guessed_letters):
    while True:
        guess = input("Enter a letter (or type 'quit' to exit): ").strip().lower()
        if guess == "quit":
            print("Thanks for playing!")
            sys.exit(0)
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetical character.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue
        return guess

def play():
    secret = choose_word()
    guessed = set()
    wrong = 0

    print("Welcome to Hangman! Guess the word one letter at a time.\n")

    while True:
        display_state(secret, guessed, wrong)

        # Check for loss
        if wrong >= MAX_WRONG:
            print(f"Game over — you lost. The word was: {secret}")
            break

        # Check for win
        if all(c in guessed for c in secret):
            print(f"Congratulations — you guessed the word: {secret} 🎉")
            break

        guess = get_guess(guessed)
        guessed.add(guess)

        if guess not in secret:
            wrong += 1
            print(f"'{guess}' is not in the word.\n")
        else:
            print(f"Nice! '{guess}' is in the word.\n")

if __name__ == "__main__":
    play()
