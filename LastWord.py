"""Accepts a string, strips white space, returns the length of the last
word in the list"""


def lengthOfLastWord(s):
    s = s.strip()
    words = s.split(' ')
    word = words[-1]
    return len(word)
