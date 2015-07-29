from os import listdir
from os.path import join
import helpers

class Corpus:

    def __init__(self):
        self.tokens = {}
        self.total_tokens = 0

    def add(self, document):
        words = helpers.get_words(document)
        for word in words:
            if word in self.tokens.keys():
                self.tokens[word] += 1  # adds each word count to the tokens list
            else:
                self.tokens[word] = 1

    def load_from_directory(self, directory):
        for file in listdir(directory):
            file_data = open(join(directory, file), 'r').read()
            for line in file_data.split('\n'):
                self.add(line)
        self.total_tokens = self.count_total_entries(self.tokens)

    def token_count(self, word):
        if word in self.tokens.keys():
            return self.tokens[word]
        else:
            return 0

    def count_total_entries(self, tokens):
        total = 0
        for index, key in enumerate(tokens):
            total += tokens[key]
        return total
