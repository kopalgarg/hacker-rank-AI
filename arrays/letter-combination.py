import string
import numpy as np

class Solution:
    def letterCombinations(self, digits: str):
        # create a mapping
        digits_range = range(2,9)
        alphabet_list = list(string.ascii_lowercase)
        letters_list = np.zeros((len(range(2,9)),3))
        alpha_n = 0
        for i in digits_range:
            for j in range(0,3):
                letters_list[i,j]=str(letters_list[i,j])
                letters_list[i,j]=alphabet_list[alpha_n]
                alpha_n+=1
        # initialize a DS that maps digits to letters

        if digits.length >=0 & digits.length <=4:
            print(letters_list)
        # contraint 1: if the input is empty, return an empty array   
        else:
            return []