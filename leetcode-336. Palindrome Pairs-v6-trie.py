from typing import List


class Trie:
    def __init__(self, word=-1):
        self.word = word
        self.map = {}

    def dfs(self, res, index):
        def helper(node, str):
            ans = []
            if node.word != -1:
                ans.append((str, node.word))
            for char in node.map:
                res = helper(node.map[char], str + char)
                ans += res
            return ans
        ans = helper(self, '')
        for a in ans:
            if a[1] != index and a[0] == a[0][::-1]:
                res.append([a[1], index])


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        root = Trie()
        ans = []

        def insert(root, word, index):
            if not word:
                root.word = index
            for i, char in enumerate(word):
                if char not in root.map:
                    node = Trie()
                    root.map[char] = node
                else:
                    node = root.map[char]
                root = node
                if i == len(word) - 1:
                    root.word = index

        for i, word in enumerate(words):
            insert(root, word, i)

        for i, word in enumerate(words):
            node, j = root, 0
            word = word[::-1]
            flag = True

            while j < len(word):
                if node.word != -1 and node.word != i:
                    if word[j:] == word[j:][::-1]:
                        ans.append([node.word, i])

                char = word[j]
                if char in node.map:
                    node = node.map[char]
                else:
                    flag = False
                    break
                j += 1

            if flag:
                node.dfs(ans, i)

        return ans


self = Solution()
print(self.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))

