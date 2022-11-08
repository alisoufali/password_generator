from argparse import ArgumentParser


class CLI(ArgumentParser):

    def __init__(self):
        super(CLI, self).__init__()
        self.add_argument("length", type=int, help="Length of the password")
        self.add_argument("-u", "--upper", action="store_true",
                          help="use upper-case letters in password")
        self.add_argument("-l", "--lower", action="store_true",
                          help="use lower-case letters in password")
        self.add_argument("-d", "--digit", action="store_true",
                          help="use digits in password")
        self.add_argument("-p", "--punc", action="store_true",
                          help="use punctuations in password")


cli = CLI()
