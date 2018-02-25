#my imports
import string
import math  # used for ceil method

from ciphers import Cipher


class Transposition(Cipher):
    def __init__(self, keyword="zebras"):
        #initialize attributes with keyword as zebras
        self.col = len(keyword)
        self.keyword = keyword
        self.COL_ORDER = self.create_col_order()
        self.GRID = self.create_columns()

    def create_col_order(self):
        #sort the column order by keyword
        col_order = {}
        sorted_keyword = sorted(self.keyword)
        for i, char in enumerate(sorted_keyword):
            col_order[char] = i + 1
        return col_order

    def create_columns(self):
        #generate the columns as an array that holds dictionaries
        #in the appropriate column order
        grid = []
        for char in self.keyword:
            for key in self.COL_ORDER:
                if char == key:
                    grid.append({ self.COL_ORDER[key]:[] })
        return grid

    def encrypt(self, text):
        # for char in message
        # replace spaces
        # look in text and if index is great than grid created sit i to the
        # remainder of the index
        # then add character to the current key
        # so each char will be added to the next column
        output = []
        text = text.upper().replace(" ", "")
        for i, char in enumerate(text):
            if i >= len(self.GRID):
                i %= len(self.GRID)

            current_key = next(iter(self.GRID[i]))
            self.GRID[i][current_key].append(char)

        #then loop through each column in the GRID
        #then loop through each key and value and compare if index
        #is equal to the key and then if so append the new characters to the column
        for i in range(1, self.col + 1):
            for col in self.GRID:
                for key, value in col.items():
                    if i == key:
                        combined_chars = "".join(value)
                        output.append(combined_chars)

        output = ''.join(output)
        #print out in words of 5
        output = ''.join(l + ' ' * (n % 5 == 4) for n, l in enumerate(output))

        return output


    def decrypt(self, text):
        #replace spaces
        #find the amount of chars that should be in each column
        #then loop through and shift columns
        #and then once reordered
        #pop off chars column by column
        #push to output
        output = []
        text = list(text.upper().replace(" ", ""))
        remainder = len(text) % self.col
        first_rows_leng = math.ceil(len(text) / self.col)
        rest_rows_leng = int(len(text) / self.col)
        for i in range(1, self.col + 1):
            for col in self.GRID:
                for key, value in col.items():
                    # print('i:' + str(i) + ' key:' + str(key) + ' grid:' + str(self.GRID))
                    if i == key:
                        current_pos = self.GRID.index(col)
                        if current_pos < remainder:
                            self.GRID[current_pos][key] = "".join(text[:first_rows_leng])
                            for x in range(0, first_rows_leng):
                                if text:
                                    text.pop(0)
                        else:
                            self.GRID[current_pos][key] = "".join(text[:rest_rows_leng])
                            for x in range(0, rest_rows_leng):
                                if text:
                                    text.pop(0)


        for i in range(0, 6):
            for col in self.GRID:
                for key, value in col.items():
                    output.append(value[i:i+1])


        return "".join(output)
