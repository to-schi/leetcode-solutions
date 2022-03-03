"""
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.
https://leetcode.com/problems/palindrome-pairs/
"""

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPalindrome(w):
            l, r = 0, len(w) - 1
            while l < r:
                if w[l] != w[r]:
                    return False
                l += 1
                r -= 1
            return True
        wordToIndex = {w: i for i, w in enumerate(words)}
        res = []
        for i, w in enumerate(words):
            for j in range(len(w)):
                # prefix(can be '') + pal
                prefix = w[:j][::-1]
                if prefix in wordToIndex and wordToIndex[prefix] != i and isPalindrome(w[j:]):
                    res.append([i, wordToIndex[prefix]])
                # pal(can be '') + suffix
                suffix = w[j:][::-1]
                if suffix in wordToIndex and wordToIndex[suffix] != i and isPalindrome(w[:j]):
                    res.append([wordToIndex[suffix], i])
            #  '' + pal
            if '' in wordToIndex and wordToIndex[''] != i and isPalindrome(w):
                res.append([wordToIndex[''], i])
        return res


    print(palindromePairs(1, ["bat", "tab", "cat"]))
