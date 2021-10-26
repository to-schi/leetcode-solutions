'''https://www.youtube.com/watch?v=AUIfTelAGVc'''
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
#
#
#

