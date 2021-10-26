from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in nums[0:len(nums)]:
            for b in nums[1:len(nums)]:
                if a + b == target and a <= b:
                    return(nums.index(a),nums.index(b))

                    
    print(twoSum(1,[3,3],6))    
#nums = [3,3]
#print(nums[0:len(nums)])
# nicht akzeptiert : (0, 0)