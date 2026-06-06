# Hangman Game
import random

# List of 5 predefined words
words = ["apple", "mango", "grape", "tiger", "house", "fish", "horse"]

# Choose a random word
word = random.choice(words)

# Create blanks
guessed_word = ["_"] * len(word)

wrong_guesses = 0
max_wrong = 6
guessed_letters = []

print("Welcome to Hangman!")

while wrong_guesses < max_wrong and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check if letter is in the word
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Game result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)