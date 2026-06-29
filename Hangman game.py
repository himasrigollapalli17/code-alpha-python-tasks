import random

# List of predefined words
words =input("enter word")

# Select a random word
secret_word = random.choice(words)

# Create blanks for the word
guessed_word = ["_"] * len(secret_word)

# Store guessed letters
guessed_letters = []

# Number of wrong attempts
wrong_guesses = 0
max_wrong = 6

print("🎮 Welcome to Hangman Game!")

# Game loop
while wrong_guesses < max_wrong and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    # Take input from user
    letter = input("Enter a letter: ").lower()

    # Check if already guessed
    if letter in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Add letter to guessed list
    guessed_letters.append(letter)

    # Check if letter is in the secret word
    if letter in secret_word:
        print("Correct Guess!")

        # Reveal correct letters
        i = 0
        while i < len(secret_word):
            if secret_word[i] == letter:
                guessed_word[i] = letter
            i += 1

    else:
        print("Wrong Guess!")
        wrong_guesses += 1

# Final result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:")
    print(secret_word)
else:
    print("\n❌ Game Over!")
    print("The word was:", secret_word)