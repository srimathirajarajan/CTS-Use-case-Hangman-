import random

def choose_random_word():
    words = ["jazz", "buzz", "hajj", "faff", "fizz", "fuzz" ]
    return random.choice(words)

def display_word_progress(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display
    
def hangman():
    secret_word = choose_random_word()
    guessed_letters = []
    attempts = 5

    print("Welcome to Hangman Game!")
    print("Guess the word.")

   
