"""
Prompt:
Given two lists, S and J, where S is all stones, and J are stones which are jewels,
return a count of S stones you have which are also J jewels

Accepted Solution Result:
Runtime: 36 ms, faster than 91.73% of Python3 online submissions for Jewels and Stones.
Memory Usage: 13.1 MB, less than 76.49% of Python3 online submissions for Jewels and Stones.
"""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        split_j = [j for j in J]
        split_s = [s for s in S]
        counting = 0
        for each in split_s:
            if each in split_j:
                counting+=1
        return counting
