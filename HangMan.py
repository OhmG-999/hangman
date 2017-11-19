########################################################################################################################
#                                                                                                                      #
#                                                 Hangman program                                                      #
#                                              created by M. Goardet                                                   #
#                                                                                                                      #
########################################################################################################################
import os

from GameSetup import GameSetup
from Guess import Guess
from DataAccess import DataAccess

# main function where all functions are called
def main():

    game = GameSetup()
    guess = Guess()
    dataaccess = DataAccess()
    goodguess = []
    badguess = []
    score = 0
    print('--  HANGMAN  --')
    print('BEGINNER = 1\nINTERMEDIATE = 2\nPRO = 3\n')
    choice = input('Please enter the number corresponding to your level:\n')

    # These variables get the appropriate file based on the user level
    file = dataaccess.choose_file(choice)
    path = os.path.expanduser('~/hangman')
    file_path = os.path.join(path, file)
    text = (dataaccess.read_file(file_path))

    # Declare a list and populate it after parsing the text file
    wordlist = []
    dataaccess.parse_text(text, wordlist)

    # These 3 variables keep track of the word chosen, the word to be guessed
    # and the number of allowed guesses
    word = game.pick_random_word(wordlist)
    word_to_be_guessed = []
    allowed_attempt = game.number_allowed_guesses(word)

    # Print an underscore for each letter that need to be guessed
    print(game.create_letter_placeholders(word, word_to_be_guessed))

    # loop until the number of allowed guesses has reached 0
    while allowed_attempt > 0:

        letter = input('Please enter your letter\n')

        # verify if the guess is a good guess
        if guess.is_good_guess(letter, word) is True:

            # verify if the guess has already been given before
            if guess.has_guess_already_been_guessed(letter, goodguess) is False:

                # search for all occurrences of the guess/letter in the word, reveal the letter in the word
                # to be guessed, add the letter to the list of good guess, decrease the allowed_attempt counter
                # add 20 points to the score
                guess.search_and_update_all_occurences(letter, word, word_to_be_guessed)
                guess.add_to_guessed_list(letter, goodguess)
                allowed_attempt = allowed_attempt - 1
                score += 20

            # if the guess/letter has already been found before, than display a message
            # but do not decrease the allowed_attempt counter
            else:
                print('You have already typed that letter before!\n')

        # if the guess/letter is a wrong guess then add it to the badguess list
        # decrease the allowed_attempt counter and remove 1 point from the score
        elif guess.is_good_guess(letter, word) is False:

            guess.add_to_guessed_list(letter, badguess)
            allowed_attempt = allowed_attempt - 1
            score -= 1

        # display to the player the word to be guessed with all good guesses/letters found
        # + the good and bad guesses lists + the number of attempt left until the game is over
        print(word_to_be_guessed)
        print('Good guesses:', goodguess)
        print('Bad guesses:', badguess)
        print('You have', allowed_attempt, 'attempts left\n')

        # this function verify if all letters in the word to be guess have been found
        finished = guess.all_letter_guessed(word_to_be_guessed)

        if finished is True:
            print('-- Congratulation! word found --\n')
            print('-- Your score is', score, 'points \n')

            break

    print('-- GAME OVER--\n')

    # collect the player name and pass the game data to be printed out in a file
    name = input('Please enter your name:\n')
    attempt_used = game.number_allowed_guesses(word) - allowed_attempt
    dataaccess.create_file(word, name, attempt_used, finished, score)


if __name__ == '__main__':
    main()