"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

Example:
Input: [3,1,2,4]
Output: [2,4,3,1]
"""


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evens=[]
        odds=[]
        for v in A:
            if v%2 == 0:
                evens.append(v)
            else:
                odds.append(v)
        return evens+odds
