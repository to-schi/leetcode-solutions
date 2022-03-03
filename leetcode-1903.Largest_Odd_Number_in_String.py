'''
You are given a string num, representing a large integer. Return the largest-valued odd 
integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
https://leetcode.com/problems/largest-odd-number-in-string/
'''

class Solution:
    def largestOddNumber(self, num: str) -> str:
        highest = "" # als Ausgabe gefordert :(
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 == 1:
                highest = (num[:i+1])
                return highest
        return highest

    print(largestOddNumber(1, "22467"))
