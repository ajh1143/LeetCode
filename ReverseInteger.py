#AJH
#Given a 32-bit signed integer, reverse digits of an integer.
#Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. 
#For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#This solution beats 90%+ of submissions in run-time

class Solution(object):
    def reverse(self, x):
        y = str(x)
        if y[0]=="-" :
            x = y[:0:-1]
            z = "-"+x
            if int(z) <= -2147483647:
                 return 0
            else:
                 return int(z)
        else:
            x = y[::-1]
            if int(x) >= 2147483647:
                 return 0
            else:
                 return int(x)
