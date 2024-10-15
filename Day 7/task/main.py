from random import choice
from hangman_words import word_list
from hangman_art import stages

chosen_word = choice(word_list)

print("Welcome to Hangman!")

placeholder = ["_" for _ in range(len(chosen_word))]

lives = 6
guesses = []

while "_" in placeholder and lives > 0:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    guesses.append(guess)

    if guess in guesses:
        print(f"You've already propose the letter {guess}!")

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"--- {lives}/6 lives left. ---")
        if lives == 0:
            print(f"--- You lose, the word was {chosen_word}. ---")
            break

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            placeholder[index] = letter

    print(" ".join(placeholder))

    if chosen_word == "".join(placeholder):
        print("--- You win! ---")
        break