
class Guess:

    # This function is a no argument constructor
    def __init__(self): pass

    # This function verify if the guess is a good guess
    def is_good_guess(self, letter, word):

        if letter in word:
            return True

        else:
            return False

    # This function is responsible to verify if the letter has already been used as a guess
    def has_guess_already_been_guessed(self, letter, guesseslist):

        if letter in guesseslist:
            return True

        else:
            return False

    # This function add the letter to the list of guessed letters
    def add_to_guessed_list(self, letter, guesseslist):

        if letter not in guesseslist:
            guesseslist.append(letter)

        return guesseslist

    # This function verify if all letters have been guessed
    def all_letter_guessed(self, word2):

        if '_' in word2:
            return False

        else:
            return True

    # This function search for all occurrences of the guess in the word
    def search_and_update_all_occurences(self, letter, word, word2):

        # iterate through each characters in the word to be found and compare it with user guess
        i = 0
        while i < len(word):
            word[i]
            if word[i] == letter:
                word2.pop(i)
                word2.insert(i, letter)
            i = i + 1

        return word2


