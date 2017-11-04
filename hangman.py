########################################################################
#                                                                      #
#                           Hangman program                            #
#                        created by M. Goardet                         #
#                                                                      #
########################################################################

# import randint function from random class to pick a random word from the word list
from random import randint as randy

# create a list of words
wordlist = 'awkward', 'bagpipes', 'banjo', 'bungler', 'croquet', 'crypt', 'dwarves', 'fervid', 'fishhook', 'fjord',\
            'gazebo', 'gypsy', 'haiku', 'haphazard', 'hyphen', 'ivory', 'jazzy', 'jiffy', 'jinx', 'jukebox', 'kayak',\
            'kiosk', 'klutz', 'memento', 'mystify', 'numbskull', 'ostracise', 'oxygen', 'pyjama', 'phlegm', 'pixel',\
            'polka', 'quad', 'quip', 'rhythmic', 'rogue', 'sphinx', 'squawk', 'swivel', 'toady', 'twelfth', 'unzip', \
            'waxy', 'wildebeest', 'yacht', 'zealous', 'zigzag', 'zippy', 'zombie'

# create a function to select a random word out of the word list
def pick_random_word(list):

    # pick a random word from the word list
    word = wordlist[randy(0, len(wordlist))]

    return word


# create an attempt method to keep track of the number of attempt available and the number of attempt left
def allowed_guesses(word):

    allowedguesses = len(word) * 2
    return allowedguesses


# main function where all functions are called
def main():

    # use print functions to ensure correct result for each functions
    word = pick_random_word(wordlist)
    print(word)
    print(allowed_guesses(word))


if __name__ == '__main__':
    main()