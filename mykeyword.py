#my imports
import string

from ciphers import Cipher


class Keyword(Cipher):
    def __init__(self, keyword):
        #initialize with keyword attribute and
        #create a key/index for the keyword
        self.keyword = keyword.upper()
        self.KEY = self.clean_keyword() + self.remove_letters()

    def clean_keyword(self):
        #clean the keyword
        # add to array if letter is not already there
        clean_word = []
        for char in self.keyword:
            if char not in clean_word:
                clean_word.append(char)
        return "".join(clean_word)

    def remove_letters(self):
        #clean the keyword then
        #remove the letters that
        #are in the keyword from the alphabet
        clean_word = self.clean_keyword()
        new_alphabet = []
        for char in string.ascii_uppercase:
            if char in clean_word:
                continue
            else:
                new_alphabet.append(char)
        return "".join(new_alphabet)

    def encrypt(self, text):
        # for char in message look up the key and then
        # push the appropriate index to output
        output = []
        text = text.upper()
        for char in text:
            try:
                alpha_index = self.KEY.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(string.ascii_uppercase[alpha_index])
        return "".join(output)

    def decrypt(self, text):
        # for char in message take the index and then apply
        # the normal alphabet compared to the key
        # push to output
        output = []
        text = text.upper()
        for char in text:
            try:
                alpha_index = string.ascii_uppercase.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.KEY[alpha_index])
        return "".join(output)
