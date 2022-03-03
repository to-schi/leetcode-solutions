'''
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.
https://leetcode.com/problems/power-of-three/
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        else:
            while n >= 1:
                n = n / 3
                if n == 1:
                    return True
            return False

    print(isPowerOfThree(1, 9))


