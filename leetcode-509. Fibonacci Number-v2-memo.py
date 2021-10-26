import timeit
class Solution:
    def fib(self, n: int, memo={}) -> int: # memoization!
        #print(memo)
        if n < 2:
            return n
        if n not in memo:
            memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)
        return memo[n]

self = Solution()
print(self.fib(20, {}))
#print(timeit.timeit(lambda: self.fib(10, {}), number=10))

#or:
#  def fib(self, n):
# 	 mem={0:1,1:1}
# 	 for index in range(2, n+1):
# 		 mem[index]=mem[index-1]+mem[index-2]
# 	return(mem[n])


