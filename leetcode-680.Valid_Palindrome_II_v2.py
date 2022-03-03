'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
https://leetcode.com/problems/valid-palindrome-ii/
'''

def validPalindrome(self, s: str) -> bool:
    l = 0
    r = len(s)-1
    while l < r:
        if s[l] == s[r]: # wenn Zeichen links/rechts gleich, weiter zur Mitte
            l += 1
            r -= 1
        else:
            return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]
    return True

print(validPalindrome(1, "annab"))
