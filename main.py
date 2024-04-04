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
    while True:
        print("\nWord:", display_word_progress(secret_word, guessed_letters))
        guess = take_user_guess()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print("Incorrect guess! Attempts left:", attempts)
            if attempts == 0:
                print("Sorry, you're out of attempts. The word was:", secret_word)
                break
        else:
            print("Correct guess!")
            if all(letter in guessed_letters for letter in secret_word):
                print("Congratulations! You guessed the word:", secret_word)
                break

if _name_ == "_main_":
    hangman()
   
