'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] 
and each integer appears once or twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.

https://leetcode.com/problems/find-all-duplicates-in-an-array/
'''


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
