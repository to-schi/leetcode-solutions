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
