'''https://leetcode.com/problems/fibonacci-number/
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
'''

class Solution:
    def fibonacci(self, n: int) -> int:
        mem = {0: 0, 1: 1}
        for i in range(2, n+1):
            mem[i] = mem[i-1]+mem[i-2]
            print(mem)
        # instead of: 
        # if n not in memo:
        # memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)
        return(mem[n])
self = Solution()
print(self.fibonacci(10))
