'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
https://leetcode.com/problems/valid-palindrome-ii/
'''

def validPalindrome(self, s: str) -> bool:
    def palindromeCheck(left, right):  # Helper function
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left = 0
    right = len(s)-1
    while left <= right:
        if s[left] != s[right]:
            return palindromeCheck(left+1, right) or palindromeCheck(left, right-1)
        left += 1
        right -= 1
    return True

print(validPalindrome(1, "ancbtna"))
