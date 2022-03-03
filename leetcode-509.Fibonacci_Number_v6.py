'''https://leetcode.com/problems/fibonacci-number/
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
'''
def fib(self, n: int) -> int:
    fibo1, fibo2 = 0, 1
    for brötchen in range(2, n+1):
        fibo1, fibo2 = fibo2, fibo1+fibo2 # "tuple swap" !?
    return fibo2 if n > 0 else 0


print(fib(1, 60))


