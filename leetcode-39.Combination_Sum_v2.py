'''Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target 
is less than 150 combinations for the given input.
https://leetcode.com/problems/combination-sum/
'''
from typing import List

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    def helper(i, current, totalsum):
        if totalsum > target: return
        if totalsum == target:
            res.append(current)
            return

        while i < len(candidates):
            if totalsum + candidates[i] > totalsum:
                helper(i, current + [candidates[i]], totalsum + candidates[i])
            i += 1
    helper(0, [], 0)
    return res
print(combinationSum(1, [2, 4, 7], 8))

