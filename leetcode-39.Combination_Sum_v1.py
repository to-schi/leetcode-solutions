'''Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target 
is less than 150 combinations for the given input.
https://leetcode.com/problems/combination-sum/
Solution by: https://www.youtube.com/watch?v=GBKI9VSKdGg'''
from typing import List
#class Solution:
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    def dfs(i, current, totalsum):
        if totalsum == target:
            res.append(current.copy()) # WHY copy() ???
            return
        if i >= len(candidates) or totalsum > target:
            return
        current.append(candidates[i])
        dfs(i, current, totalsum + candidates[i])
        current.pop()
        dfs(i+1, current, totalsum)
    dfs(0, [], 0)
    return res

print(combinationSum(1, [2, 4, 7], 8))
#accepted
