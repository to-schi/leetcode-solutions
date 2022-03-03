'''
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.
https://leetcode.com/problems/power-of-three/
'''

import numpy as np
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 0: return False
        else:
            ternary = np.base_repr(n, base=3)
            print(ternary)
            if 1 == sum(int(x) for x in ternary):
                return True
            else:
                return False
#working
    print(isPowerOfThree(1, 9))
