'''Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
https://leetcode.com/problems/palindrome-number/'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        return x_str == x_str[::-1]
 
    ans = isPalindrome(1,24542) # example (self, x)
    if ans:
        print("Yes")
    else:
        print("No")
# working!


