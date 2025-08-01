import random
from replit import clear
from hangman_words import word_list

chosen_word = random.choice(word_list)

lives = 6

from hangman_art import logo, stages
print(logo)

print(f'Psst, the solution is {chosen_word}.')

display = []

word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")


    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
# Uncomment the following lines to test the code with a specific guess
# for letter in chosen_word:
#     if letter == guess:
#         print(f"Good job! The letter '{guess}' is in the word.")
#     else:
#         print(f"Sorry, the letter '{guess}' is not in the word.")

