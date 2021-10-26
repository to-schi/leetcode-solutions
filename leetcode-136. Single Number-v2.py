from typing import List
def singleNumber(self, nums: List[int]) -> int:
    #print(nums.count(nums[4]))  # res = None
    #x = 2*sum(set(nums)) - sum(nums)
    a = 0
    for i in nums:
        a ^= i
    return a
print(singleNumber(1, [1, 1, 2, 2, 3]))

