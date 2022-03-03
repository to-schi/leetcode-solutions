'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
https://leetcode.com/problems/single-number/
'''
from typing import List
def singleNumber(self, nums: List[int]) -> int:
    a = 0
    for i in nums:
        a ^= i
    return a
print(singleNumber(1, [1, 1, 2, 2, 3]))

