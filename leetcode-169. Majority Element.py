from typing import List
def majorityElement(self, nums: List[int]) -> int:
    s = set(nums)
    l = {}
    if len(nums) == 1:
        return nums[0]
    else:
        for num in s:
            l.update({num: nums.count(num)})
        print(l)    
        return max(l, key=l.get)

print(majorityElement(1, [0]))



