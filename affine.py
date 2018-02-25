#my imports
import string

from ciphers import Cipher


class Affine(Cipher):
    def __init__(self, multiplier=5, offset=8, divisor=26):
        #initialize affine cipher with attributes
        self.multiplier = multiplier
        self.offset = offset
        self.divisor = divisor

    def encrypt(self, text):
        #for each character in message multiply by multiplier
        # add by the offset
        # and get the remainder of all of that divided by the divisor
        # append it to output
        output = []
        text = text.upper()
        for char in text:
            try:
                alpha_index = (self.multiplier * string.ascii_uppercase.index(char) + self.offset) % self.divisor
            except ValueError:
                output.append(char)
            else:
                output.append(string.ascii_uppercase[alpha_index])
        return "".join(output)

    def decrypt(self, text):
        #for each character in message
        #reset the multiplier to 21
        # subtract by the offset and divide by divisor
        # return remainder and append it to output
        output = []
        text = text.upper()
        self.multiplier = 21
        for char in text:
            try:
                alpha_index = (self.multiplier * (string.ascii_uppercase.index(char) - self.offset)) % self.divisor
            except ValueError:
                output.append(char)
            else:
                output.append(string.ascii_uppercase[alpha_index])
        return "".join(output)
