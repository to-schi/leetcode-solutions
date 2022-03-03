'''
Given a string s consisting of some words separated by some number of spaces, 
return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
https://leetcode.com/problems/length-of-last-word/'''


def lengthOfLastWord(self, s: str) -> int:
    sentence = s.split()
    return len(sentence[-1])

print(lengthOfLastWord(1, " moon  "))
# working!
