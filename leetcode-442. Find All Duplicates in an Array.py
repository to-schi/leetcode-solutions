from typing import List
def findDuplicates(self, nums: List[int]) -> List[int]:

        hashmap = {e : 0 for e in nums}
        ans = []
        print(hashmap)
        for num in nums:
            if hashmap[num] == 0:
                hashmap[num] += 1
            else:
                ans.append(num)

        return ans
print(findDuplicates(1, [1,2,3,3,4,5,6,6,7]))
    #     def findDuplicates(self, nums: List[int]) -> List[int]:
    # out = []
    # for n in nums:
    #     if nums.count(n) > 1:
    #         if n in out:
    #             continue
    #         else:
    #             out.append(n)
    # return out
#print(findDuplicates(1, [1]))

# working but slow


# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         result = []
#         for i in range(len(nums)):
#             index = abs(nums[i]) - 1
#             if nums[index] < 0:
#                 result.append(abs(nums[i]))
#             else:
#                 nums[index] *= -1
#         return result

# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         i, l = 0, len(nums)
#         while i < l:
#             c_i = nums[i]-1
#             if nums[c_i] != nums[i]:  # element is at wrong index
#                 nums[i], nums[c_i] = nums[c_i], nums[i]  # swap
#             else:
#                 i += 1
#         ans = [nums[i] for i in range(l) if nums[i] != i + 1]
#         return ans

# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         nums.append(0)
#         ans = []
#         for i in range(len(nums)):
#             val = nums[i]
#             if val < 0:
#                 nextIndex = (0 - val) - i
#             else:
#                 nextIndex = val

#             if nums[nextIndex] < 0:
#                 ans.append(nextIndex)
#             else:
#                 nums[nextIndex] = 0 - (nums[nextIndex] + nextIndex)
#         return ans
