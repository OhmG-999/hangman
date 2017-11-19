import datetime


class DataAccess:
    # Default constructor
    def __init__(self): pass

    # This function is responsible to return the correct file name corresponding to the
    # the player level
    def choose_file(self, choice):
        filename = 'Level' + choice + '.txt'
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

    # This function create a file and add the player details
    def create_file(self, word, name, attempt_used, result, score):
        file_name = 'Log - {:%Y-%m-%d %H:%M:%S}.txt'.format(datetime.datetime.now())
        file = open(file_name, 'w')
        content = format('################################\nWord: %s\nNumber of attempt used: %s\n'
                         'Was the word found?: %s\nPlayer name: %s\nScore: %s\n'
                         '################################\n' % (word, attempt_used, result, name, score))
        file.write(str(content))
        file.close()
