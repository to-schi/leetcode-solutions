'''
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
https://leetcode.com/submissions/detail/572047385/
'''
def strStr(self, haystack: str, needle: str) -> int:
    if len(haystack) == 0 and len(needle) == 0:
        return 0
    if len(needle) == 0:
        return 0
    if needle in haystack:
        return haystack.find(needle)
    else:
        return -1

print(strStr(1, "Hello", "lo"))

