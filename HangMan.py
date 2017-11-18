########################################################################################################################
#                                                                                                                      #
#                                                 Hangman program                                                      #
#                                              created by M. Goardet                                                   #
#                                                                                                                      #
########################################################################################################################

from GameSetup import GameSetup
from Guess import Guess

game = GameSetup()
guess = Guess()

goodGuess = Guess()
goodGuess = []
badGuess = Guess()
badGuess = []

# create a list of words
wordslist = 'awkward', 'bagpipes', 'banjo', 'bungler', 'croquet', 'crypt', 'dwarves', 'fervid', 'fishhook', 'fjord',\
            'gazebo', 'gypsy', 'haiku', 'haphazard', 'hyphen', 'ivory', 'jazzy', 'jiffy', 'jinx', 'jukebox', 'kayak',\
            'kiosk', 'klutz', 'memento', 'mystify', 'numb', 'ostracise', 'oxygen', 'pyjama', 'phlegm', 'pixel',\
            'polka', 'quad', 'quip', 'rhythmic', 'rogue', 'sphinx', 'squawk', 'swivel', 'toady', 'twelfth', 'unzip', \
            'waxy', 'wildebeest', 'yacht', 'zealous', 'zigzag', 'zippy', 'zombie'


# main function where all functions are called
def main():

    # These 4 variables keep track of the word chosen, the word to be guessed,
    # the number of allowed guesses and if the word has been fully guessed
    word = game.pick_random_word(wordslist)
    word_to_be_guessed = []
    allowed_attempt = game.number_allowed_guesses(word)
    finished = guess.all_letter_guessed(word_to_be_guessed)
    print(finished)

    print(game.create_letter_placeholders(word, word_to_be_guessed))

    while allowed_attempt > 0:

        letter = input('Please enter your letter\n')

        if guess.is_good_guess(letter, word) is True:

            if guess.has_guess_already_been_guessed(letter, goodGuess) is False:

                guess.add_to_guessed_list(letter, goodGuess)
                guess.search_and_update_all_occurences(letter, word, word_to_be_guessed)

            else:
                print('You have already typed that letter before!\n')

        else:
            guess.add_to_guessed_list(letter, badGuess)

        print(word_to_be_guessed)
        print('Good guesses:', goodGuess)
        print('Bad guesses:', badGuess)
        allowed_attempt = allowed_attempt - 1
        print(allowed_attempt)
        finished = guess.all_letter_guessed(word_to_be_guessed)
        print(finished)
        print(word)

        if finished is True:
            print('-- Congratulation! word found --')
            break

    print('-- GAME OVER--')


if __name__ == '__main__':
    main()