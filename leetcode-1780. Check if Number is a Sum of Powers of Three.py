class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        res = 0
        for e in range(n,0):
            res = res + 3**e
            if res == n:
                return True
            # elif res > n:
            #     return False
            else:
                continue

    print(checkPowersOfThree(1, 91))  # 21 False
    # not working!
#e in range(n,0)

# if 3*e == n: return True
# else:
#     res = 
# 3**0 + 3**1 + 3**2 == n return True