'''
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target
is less than 150 combinations for the given input.
https: // leetcode.com/problems/combination-sum/
Solution by:
https://www.youtube.com/watch?v=AUIfTelAGVc'''
from typing import List
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    # make a list of empty lists with indexes 0 to target+1
    dp = [[] for _ in range(target+1)] # +1 -> one for the zero (dynamic programming)
    for c in candidates:
        for i in range(1, target+1):
            if i < c: continue
            if i == c:
                dp[i].append([c]) # append the candidate to list inside dp if index is equal
            else:
                for sub_list in dp[i-c]: # current numer i minus candidate
                    dp[i].append(sub_list+[c]) # for each sub_list append sub_list-value and c-value (?)
    return dp[target]


print(combinationSum(1, [2, 4, 7], 8))

# target-steps:    1  2   3    4     5      6       7
# candidates fit: [] [2] [3] [2,2] [2,3] [2,2,2] [2,2,3]
# dp:                                    [3,3]   [7]
#                                        [6]

