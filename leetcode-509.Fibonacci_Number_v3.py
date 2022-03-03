'''https://leetcode.com/problems/fibonacci-number/
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
'''

# Solution 4 - O(1) space & O(n) time
# WTF????????
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a = 0
        b = 1
        for brötchen in range(2, n+1):
            c = a + b
            a = b
            b = c
        return c
self = Solution()
print(self.fib(496))




# Solution 3 (DP - Bottom Up - Tabulation)
# class Solution:
#     def fib(self, n: int) -> int:
#         lookup = [0, 1] + [-1]*(n-1)
#         for i in range(2, n+1):
#             lookup[i] = lookup[i-1] + lookup[i-2]
#         return lookup[n]
