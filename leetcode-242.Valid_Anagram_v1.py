'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
https://leetcode.com/problems/valid-anagram/
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            rem = list(t)
            for c in s:
                if c in rem:
                    rem.remove(c)
                    if len(rem) == 0:
                        return True
                else:
                    return False

    print(isAnagram(1, "rac", "car" ))
# working!
