from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for idx, num in enumerate(nums):
            dict_nums[num] = idx
        for idx, num in enumerate(nums):
            if target - num in dict_nums and idx != dict_nums[target - num]:
                return [idx + 1, dict_nums[target - num] + 1] # twoSum II -> +1

    print(twoSum(1,[3,3],6))
    # working!
