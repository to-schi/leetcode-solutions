'''
You are given a string s. You can convert s to a palindrome by adding characters in front of it.
Return the shortest palindrome you can find by performing this transformation.
https://leetcode.com/problems/shortest-palindrome/
'''
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        pal =[]
        fr = -1
        to = 0
        for char in s:
            pal.append(char)
        while pal != pal[::-1]:
            pal.insert(to, pal[fr])
            fr += -1
            to += 1
        return ("".join(pal))

    print(shortestPalindrome(1, "annab"))
    #working!

# copy letzen to front
#     check
# copy vorletzen to front+1
#     check
#You are given a string s. You can convert s to a palindrome by adding characters in front of it.
# Return the shortest palindrome you can find by performing this transformation.

# Example 1:
# Input: s = "aacecaaa"
# Output: "aaacecaaa"

# Example 2:
# Input: s = "abcd"
# Output: "dcbabcd"

# Constraints:
#     0 <= s.length <= 5 * 104
#     s consists of lowercase English letters only.
