'''
Given two binary strings a and b, return their sum as a binary string.
https://leetcode.com/problems/add-binary/
'''


def addBinary(self, a: str, b: str) -> str:
     sum = (int(a, 2)+int(b, 2))
     return format(int(a, 2)+int(b, 2), "0b")

print(addBinary(1, "0", "1011"))
