import random

def play_hangman():
    # Predefined list of 5 words as per internship instructions
    words = ['python', 'software', 'logic', 'coding', 'github']
    target_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("--- Welcome to CodeAlpha Hangman! ---")
    print(f"The word has {len(target_word)} letters.")

    while attempts > 0:
        # Create the display word (e.g., "_ y _ _")
        display_word = ""
        for letter in target_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print(f"\nWord: {display_word}")
        print(f"Attempts remaining: {attempts}")
        
        # Check if user has won
        if "_" not in display_word:
            print("Congratulations! You guessed the word correctly!")
            break

        # Get user input
        guess = input("Guess a letter: ").lower()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        # Process the guess
        guessed_letters.append(guess)
        
        if guess in target_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Wrong guess! '{guess}' is not there.")
            attempts -= 1

    if attempts == 0:
        print(f"\nGame Over! The word was: {target_word}")

if __name__ == "__main__":
    play_hangman()