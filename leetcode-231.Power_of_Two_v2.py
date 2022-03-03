'''
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
https://leetcode.com/problems/power-of-two/
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
    # count all 1s in binary format
        #print(bin(n))
        if n > 0 and bin(n).count("1") == 1:
            return True
        else:
            return False
    print(isPowerOfTwo(1, 16))


