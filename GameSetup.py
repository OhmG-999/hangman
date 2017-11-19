
# import randint function from random class to pick a random word from the word list
from random import randint as randy


class GameSetup:

    # This function is a no argument constructor
    def __init__(self): pass

    # This function is responsible to pick a random word from a word list
    def pick_random_word(self, list_of_word):

        word = list_of_word[randy(1, len(list_of_word))]

        return word

    # This function is responsible to calculate the number of allowed guesses
    def number_allowed_guesses(self, word):

        allowed_guesses = len(word) * 2

        return allowed_guesses

    # This function create an underscore placeholder for each letter
    def create_letter_placeholders(self, word, word2):

        for i in range(len(word)):
            word2.insert(i, '_')

        return word2






