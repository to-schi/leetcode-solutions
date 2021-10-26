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

