import math
class Solution:
    def fib(self, n: int) -> int:
	# Ref: http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html
        return round(pow((1 + math.sqrt(5)) / 2, n) / math.sqrt(5))

self = Solution()
print(self.fib(496))
print(math.sqrt(5))
#working!
# one-liner:
# class Solution:
#     def fib(self, n: int) -> int:
#         return (int)((1 / (5**0.5)) * ((((1 + (5**0.5)) / 2)**n) - (((1 - (5**0.5)) / 2)**n)))
