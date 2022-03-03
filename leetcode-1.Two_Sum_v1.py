'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
https://leetcode.com/problems/two-sum/'''


from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = {}
        solution = []
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if num in complementMap:
                return [complementMap[num], i]
            else:
                complementMap[complement] = i

    print(twoSum(0,[2,3,4],6))
# working!
    # Für mehrere Lösungen:
    #
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     complementMap = {}
    #     solutions = []
    #     for i in range(len(nums)):
    #         num = nums[i]
    #         complement = target - num
    #         if num in complementMap:
    #             solutions.extend((complementMap[num], i))
    #         else:
    #             complementMap[complement] = i
    #     # return solutions
    # print(twoSum(1, [2, 3, 3, 4], 6))

    # >>> [1, 2, 0, 3]
