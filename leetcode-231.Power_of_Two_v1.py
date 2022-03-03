'''
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
https://leetcode.com/problems/power-of-two/
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n >= 1:
            n = n / 2
            if n == 0.5:
                return True
        return False
    print(isPowerOfTwo(1, 128))
