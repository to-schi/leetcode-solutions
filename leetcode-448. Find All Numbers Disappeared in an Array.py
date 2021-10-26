from typing import List
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    sec = list(range(1, len(nums)+1))
    return list(set(sec) - set(nums))

print(findDisappearedNumbers(1, [1,2,4,6,7]))

#Given an array nums of n integers where nums[i] is in the range[1, n], 
# return an array of all the integers in the range [1, n] that do not appear in nums.

# def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#     #nums_sort = sorted(nums)
#     set = list(range(1, len(nums)+1))
#     ans = []
#     for n in set:
#         if n not in nums:
#             ans.append(n)
#     return ans
# print(findDisappearedNumbers(1, [0]))
# # working, but Time Limit Exceeded
