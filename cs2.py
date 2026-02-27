import random

def scramble_word(word):
    """Returns the letters of a word in a random order."""
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def play_game():
    # 1. Predefined list of at least 10 words
    word_bank = [
        "python", "jupiter", "algorithm", "variable", "function",
        "keyboard", "monitor", "software", "database", "circuit"
    ]
    
    # 2. Randomly select a word
    original_word = random.choice(word_bank)
    
    # 3. Scramble the letters
    scrambled = scramble_word(original_word)
    
    # 4. Set game variables
    attempts = 3
    print("--- Welcome to the Word Scramble Challenge! ---")
    print(f"Scrambled word: {scrambled}")
    
    # 5. Game Loop
    while attempts > 0:
        guess = input(f"\n({attempts} attempts left) Your guess: ").strip().lower()
        
        if guess == original_word:
            print(f"🎉 Correct! The word was indeed '{original_word}'.")
            return # Exit the function as a winner
        else:
            attempts -= 1
            if attempts > 0:
                print("Incorrect! Try again.")
            else:
                # 6. Reveal word if player fails
                print(f"Game Over! The correct word was '{original_word}'.")

if __name__ == "__main__":
    play_game()