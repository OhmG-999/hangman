
class DataAccess:

    # Default constructor
    def __init__(self): pass

    # This function is responsible to return the correct file name corresponding to the
    # the player level
    def choose_file(self, choice):

        filename = 'Level'+choice+'.txt'
        return filename

    # This function read a text file
    def read_file(self, file):

        text = open(file)

        return text

    # This function parse the text file
    def parse_text(self, text, mylist):

        for word in text.readline().split(', '):
            mylist.append(word)

        return mylist