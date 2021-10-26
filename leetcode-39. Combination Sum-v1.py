'''https://www.youtube.com/watch?v=GBKI9VSKdGg'''
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




#     remainder = target
#     if target == 0:
#         return out
#     if target < 0:
#         return out
#     for num in candidates:
#         remainder = target - num
#         if remainder < 0:
#             candidates.remove(num)
#         if remainder > 0 and remainder > min(candidates):
#             out.append(num)
#             #combinationSum(1, candidates, remainder, out)
#         if remainder == target:
#             out.append(num)
#     return combinationSum(1, candidates, target, out)
# print(combinationSum(1, [2, 4, 7], 8, []))





# def canSum(targetSum, numbers, memo={}):
#     if targetSum in memo:
#         return memo[targetSum]
#     if targetSum == 0:
#         return True
#     if targetSum < 0:
#         return False
#     for num in numbers:
#         remainder = targetSum - num
#         if canSum(remainder, numbers, memo) == True:
#             return True
#             #memo[targetSum]
#     memo[targetSum] = False
#     return False
# print(canSum(300, [7, 14], {}))



