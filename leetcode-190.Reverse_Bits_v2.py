'''
Reverse bits of a given 32 bits unsigned integer.
https://leetcode.com/problems/reverse-bits/
'''

def reverseBits(self, n: int) -> int:
    b = bin(n)[2:]
    b_rev = b[::-1]
    while len(b_rev) < 32:
        b_rev += '0'
    dec = int(b_rev, 2)
    return dec


print(reverseBits(1, 43261596))
