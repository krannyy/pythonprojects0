import random

from hangman_words import word_list

from hangman_art import stages

from hangman_art import logo

print(logo)



# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
alr_guessed = []
lives = 6
print(f"You start with {lives} lives")

while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in alr_guessed:
        print(f"You have already guessed this letter: {alr_guessed}")
    alr_guessed.append(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"Now you have: {lives}, lives left")

    print(display)

    # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."

    if "_" not in display:
        game_over = True
        print("You win.")
    if lives <= 0:
        game_over = True
        print("You lose!")
    

    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.