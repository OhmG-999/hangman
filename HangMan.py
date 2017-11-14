########################################################################################################################
#                                                                                                                      #
#                                                 Hangman program                                                      #
#                                              created by M. Goardet                                                   #
#                                                                                                                      #
########################################################################################################################

import GameSetup as Game

# create a list of words
wordlist = 'awkward', 'bagpipes', 'banjo', 'bungler', 'croquet', 'crypt', 'dwarves', 'fervid', 'fishhook', 'fjord',\
            'gazebo', 'gypsy', 'haiku', 'haphazard', 'hyphen', 'ivory', 'jazzy', 'jiffy', 'jinx', 'jukebox', 'kayak',\
            'kiosk', 'klutz', 'memento', 'mystify', 'numb', 'ostracise', 'oxygen', 'pyjama', 'phlegm', 'pixel',\
            'polka', 'quad', 'quip', 'rhythmic', 'rogue', 'sphinx', 'squawk', 'swivel', 'toady', 'twelfth', 'unzip', \
            'waxy', 'wildebeest', 'yacht', 'zealous', 'zigzag', 'zippy', 'zombie'

# create 2 lists of guesses: good and bad
goodguesses = []
badguesses = []
word_to_be_guessed = []


# create a function to display the letter guessed
def display_word_to_be_guessed(letter, word, word2):

    # iterate through each characters in the word to be searched
    for i, ii in enumerate(word):
        if letter == ii:
            word2.pop(i)
            word2.insert(i, letter)
        else:
            print('dans le luc')

    print(word2)


# main function where all functions are called
def main():

    # use print functions to ensure correct result for each functions
    word = Game.pick_random_word(wordlist)
    print(word)
    print(Game.number_allowed_guesses(word))
    print(Game.create_letter_placeholders(word, word_to_be_guessed))

    player_letter = input('Enter your letter\n')
    # display_word_to_be_guessed(player_letter, word, word_to_be_guessed)


if __name__ == '__main__':
    main()