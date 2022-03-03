'''https://leetcode.com/problems/fibonacci-number/
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
'''

# Fibonacci: 1st+2nd etc.: 1 1 2 3 5 8 13 21 34
#working                   1 2 3 4 5 6 7  8  9
# my first solution:
from functools import lru_cache
class Solution:
    @lru_cache # like memoization! only with integers (not lists)
    def fib(self, n: int) -> int:
        if n == 0:
            return 0 
        if n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)

self = Solution()
print(self.fib(496))

# Iterative:
# class Solution:
#     def fib(self, n: int) -> int:
#         prev, value = 1, 0
#         for _ in range(n):
#             # swap two values at first time
#             value = prev + (prev := value)
#         return value
