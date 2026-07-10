import random

# List of words
words = ["python", "programming", "computer", "hangman", "developer"]

# Choose a random word
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman!")

while wrong_guesses < max_wrong_guesses:
    # Display the word with underscores for unguessed letters
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word)

    # Check if the word is completely guessed
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        wrong_guesses += 1
        print(f"Wrong guess! Attempts left: {max_wrong_guesses - wrong_guesses}")

else:
    print("\nGame Over! The word was:", word)