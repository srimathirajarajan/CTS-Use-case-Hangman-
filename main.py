
def take_user_guess():
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic character.")
        return take_user_guess()
    return guess

def hangman():
    secret_word = choose_random_word()
    guessed_letters = []
    attempts = 5

    print("Welcome to Hangman Game!")
    print("Guess the word.")

   
