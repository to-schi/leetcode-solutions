'''
Write a function that takes an unsigned integer and returns 
the number of '1' bits it has (also known as the Hamming weight).
https://leetcode.com/problems/number-of-1-bits/
'''

def hammingWeight(self, n: int) -> int:
    b = str(bin(n))
    weight = b.count('1')
    return weight

print(hammingWeight(1, 3))
# working!
