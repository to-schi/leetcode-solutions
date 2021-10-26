from typing import List

def removeElement(self, nums: List[int], val: int) -> int:
    for i in reversed(range(0, len(nums))):
        if nums[i] == val:
            nums.pop(i)
    return len(nums)

print(removeElement(1, [0,1,2,2,3,0,4,2], 2))
#working, aber mit return len(nums) nicht nums(????)


#assert(Solution().removeElement(1, [0, 1, 2, 2, 3, 0, 4, 2], 2) == [0, 1, 3, 0, 4])
