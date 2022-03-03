'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
https://leetcode.com/problems/valid-palindrome-ii/
'''


def validPalindrome(self, s: str) -> bool: 
    pal = []
    res = []
    for char in s:
        pal.append(char)
    if pal == pal[::-1]:
        return True
    else:
        for i in range (0,len(pal)):
            res.append(pal[i])
            pal.pop(i)
            if pal != pal[::-1]:
                pal.insert(i, res[0])
                res.pop(0)
            else:
                return True
        return False
print(validPalindrome(1, "anckna"))
#working, but not accepted - time limit

