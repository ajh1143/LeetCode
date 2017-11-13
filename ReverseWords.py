#Given an input string, reverse the string word by word.
#For example,
#Given s = "the sky is blue",
#return "blue is sky the".

class Solution(object):
    def reverseWords(self, s):
        self.s = s
        splitter = self.s.split()
        reverser = splitter[::-1]
        rejoiner = " ".join(reverser)
        return rejoiner
