from typing import List
def singleNumber(self, nums: List[int]) -> int:
    return (2*sum(set(nums)) - sum(nums))
print(singleNumber(1, [1, 1, 2, 2, 3, 3, 5]))
