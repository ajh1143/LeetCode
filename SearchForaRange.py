#Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
#Your algorithm's runtime complexity must be in the order of O(log n).
#If the target is not found in the array, return [-1, -1].
#
#For example,
#Given [5, 7, 7, 8, 8, 10] and target value 8,
#return [3, 4].


class Solution(object):
   def searchRange(self, nums, target):
        #given ascending list of nums
        #given target number
        #find if target matches positions in nums
        #if target in nums, return indices from first and final positions
        #if target not in nums, return [-1,-1]
        list = []
        failedList = [-1,-1]
        match = 0
        index = 0
        for each in nums:
            if target == each:
                match += 1
                list.append(index)
            index +=1
        if match == 0:
            return failedList
        if match == 1:
            otherList = [list[0], list[0]]
            return otherList
        else:
            maxList = max(list)
            minList = min(list)
            finalList = [minList, maxList]
            return finalList
