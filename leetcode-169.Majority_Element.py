'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
https://leetcode.com/problems/majority-element/
'''

from typing import List
def majorityElement(self, nums: List[int]) -> int:
    s = set(nums)
    l = {}
    if len(nums) == 1:
        return nums[0]
    else:
        for num in s:
            l.update({num: nums.count(num)})
        #print(l)    
        return max(l, key=l.get)

print(majorityElement(1, [1,2,2,1,1]))



