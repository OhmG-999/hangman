########################################################################################################################
#                                                                                                                      #
#                                                 Hangman program                                                      #
#                                              created by M. Goardet                                                   #
#                                                                                                                      #
########################################################################################################################

from GameSetup import GameSetup
from Guess import Guess



# create a list of words
wordslist = 'awkward', 'bagpipes', 'banjo', 'bungler', 'croquet', 'crypt', 'dwarves', 'fervid', 'fishhook', 'fjord',\
            'gazebo', 'gypsy', 'haiku', 'haphazard', 'hyphen', 'ivory', 'jazzy', 'jiffy', 'jinx', 'jukebox', 'kayak',\
            'kiosk', 'klutz', 'memento', 'mystify', 'numb', 'ostracise', 'oxygen', 'pyjama', 'phlegm', 'pixel',\
            'polka', 'quad', 'quip', 'rhythmic', 'rogue', 'sphinx', 'squawk', 'swivel', 'toady', 'twelfth', 'unzip', \
            'waxy', 'wildebeest', 'yacht', 'zealous', 'zigzag', 'zippy', 'zombie'


# main function where all functions are called
def main():

    game = GameSetup()
    guess = Guess()
    goodguess = []
    badguess = []
    score = 0

    # These 3 variables keep track of the word chosen, the word to be guessed
    # and the number of allowed guesses
    word = game.pick_random_word(wordslist)
    word_to_be_guessed = []
    allowed_attempt = game.number_allowed_guesses(word)

    print(game.create_letter_placeholders(word, word_to_be_guessed))

    while allowed_attempt > 0:

        letter = input('Please enter your letter\n')

        if guess.is_good_guess(letter, word) is True:

            if guess.has_guess_already_been_guessed(letter, goodguess) is False:

                guess.search_and_update_all_occurences(letter, word, word_to_be_guessed)
                guess.add_to_guessed_list(letter, goodguess)
                allowed_attempt = allowed_attempt - 1
                score += 20

            else:
                print('You have already typed that letter before!\n')

        elif guess.is_good_guess(letter, word) is False:

            guess.add_to_guessed_list(letter, badguess)
            allowed_attempt = allowed_attempt - 1
            score -= 1

        print(word_to_be_guessed)
        print('Good guesses:', goodguess)
        print('Bad guesses:', badguess)
        print('You have', allowed_attempt, 'attempts left\n')
        finished = guess.all_letter_guessed(word_to_be_guessed)

        if finished is True:
            print('-- Congratulation! word found --')
            break

    print('-- GAME OVER--\n')
    print('-- Your score is', score, 'points \n')


if __name__ == '__main__':
    main()