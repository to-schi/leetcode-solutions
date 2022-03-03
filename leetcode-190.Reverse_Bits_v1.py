'''
Reverse bits of a given 32 bits unsigned integer.
https://leetcode.com/problems/reverse-bits/
'''


def reverseBits(self, n: int) -> int:
    b = format(n, "032b")
    b_rev = b[::-1]
    dec = int(b_rev, 2)
    return dec
print(reverseBits(1, 43261596))

