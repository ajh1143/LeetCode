"""Accepts a list of integers as 'digits', combines them, adds 1 to the overall value, and returns a new list of integers"""

class Solution(object):
    def plusOne(self, digits):
        expand_digits = []
        combine_digits = int(''.join(map(str,digits)))
        add_one = combine_digits+1
        for x in str(add_one):
            expand_digits.append(x) 
        out_num = map(int, expand_digits)
        return(out_num)
