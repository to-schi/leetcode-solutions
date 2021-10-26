# Solution 4 - O(1) space & O(n) time
# WTF????????
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a = 0
        b = 1
        for brötchen in range(2, n+1):   # i?????
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
