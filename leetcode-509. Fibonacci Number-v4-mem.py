class Solution:
    def fibonacci(self, n: int) -> int:
        mem = {0: 0, 1: 1}
        for i in range(2, n+1):
            mem[i] = mem[i-1]+mem[i-2]
            print(mem)
        # statt: 
        # if n not in memo:
        # memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)
        return(mem[n])
self = Solution()
print(self.fibonacci(10))
