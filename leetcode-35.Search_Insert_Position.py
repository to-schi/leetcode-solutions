'''
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, 
return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
https://leetcode.com/problems/search-insert-position/
'''

from typing import List
def searchInsert(self, nums: List[int], target: int) -> int:
    if len(nums) == 1:
        if target <= nums[0]:
            return 0
        else:
            return 1
    else:
        for i in range(0, len(nums)):
            if target < nums[i]:
                return i
            elif target == nums[i]:
                return i
            elif nums[i] < target < nums[i+1]:
                return i+1
            elif target > nums[-1]:
                return len(nums)
print(searchInsert(1,[1,3], 2))
# working!
