''' https://www.youtube.com/watch?v=D5PMCyPcw-o '''
import collections
from typing import List
class Solution:
    class TrieNode(collections.defaultdict):
        def __init__(self):
            super().__init__(Solution.TrieNode)
            self.word_idx = -1
            self.list = []

    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        def partial_palindrome(w, l):
            r = len(w)-1
            while l < r:
                if w[l] != w[r]: return False
                l += 1
                r -= r
            return True
        #populating the trie
        root = Solution.TrieNode()
        for i, word in enumerate(words):
            node = root
            reversed_word = word[::-1]
            for j, char in enumerate(reversed_word):
                if partial_palindrome(reversed_word, j):
                    node.list.append(i)
                node = node[char]
            node.word_idx = i

        pairs = []
        # find the pairs
        for i, word in enumerate(words):
            node = root
            #reversed_word = word[::-1]
            for j, char in enumerate(word):
                # case 3: word[j] is longer than a possible word[i]
                if node.word_idx != -1 and partial_palindrome(word, j):
                    pairs.append([i, node.word_idx]) 
                if char not in node: break
                node = node[char]
            else:
                # case 1: word[i] == word[j][::-1]
                if node.word_idx not in [-1, i]:
                    pairs.append([i, node.word_idx])
                # case 2: word[i] is "abc+palindrome" & word[j] "cba"    
                for k in node.list:
                    pairs.append([i, k])
        return pairs


self = Solution()
#print(self.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
print(self.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
                    

