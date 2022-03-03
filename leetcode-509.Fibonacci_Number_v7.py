'''https://leetcode.com/problems/fibonacci-number/
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
'''

def fib(self, n: int) -> int:
    f = list((0, 1))
    for x in range(1, n):
        f.append(f[-1] + f[-2])
    else:
        return f[-1]

print(fib(1, 496))

