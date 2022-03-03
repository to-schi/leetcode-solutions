
'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers 
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array 
[index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''

from typing import List
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    dict_nums = {}
    for idx, num in enumerate(numbers):
        dict_nums[num] = idx
    for idx, num in enumerate(numbers):
        if target - num in dict_nums and idx != dict_nums[target - num]:
            return [idx + 1, dict_nums[target - num] + 1]

print(twoSum(1, [1,2,3,4,5,6], 7))
# working!
