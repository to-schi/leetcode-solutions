"""
Time: O(N x L^2), assume the average length of word is L. Note that, eversing the string takes O(L).
Space: O(L), beside from ans, need `left` and `right` constantly to store the word.
"""
class Solution(object):
    def palindromePairs(self, words):
        ans = set()
        index = {word: i for i, word in enumerate(words)}

        for i, word in enumerate(words):
            for j in range(len(word)+1):
                left = word[:j]
                right = word[j:]
                # check if any other word that concat to the left will make palindrome: "OTHER_WORD+`left`+`right`"
                # The above will be palindrome only if
                # 1. `left` is palindrome (left==left[::-1])
                # 2. Exsit an "OTHER_WORD" in word in words that equals to the reverse of `right` (right[::-1] in index and index[right[::-1]]!=i).
                if left == left[::-1]:
                    if right[::-1] in index and index[right[::-1]] != i:
                        ans.add((index[right[::-1]], i))

                # check if any other word that concat to the right will make palindrome: "`left`+`right`+OTHER_WORD"
                # The above will be palindrome only if
                # 1. `rihgt` is palindrome (right==right[::-1])
                # 2. Exsit an "OTHER_WORD" in words that equals to the reverse of `left` (left[::-1] in index and index[left[::-1]]!=i).
                if right == right[::-1]:
                    if left[::-1] in index and index[left[::-1]] != i:
                        ans.add((i, index[left[::-1]]))
        return ans
    print(palindromePairs(1, ["bat", "tab", "cat"]))
    
    #["babababbbaaa","bbaabbbaabbbbba","abbbbbbbbbbbb","bbabaaababb","aabbbaaaababbbbba","aabbababbab","abaaa","aba","abaab","aabbbababa","aabbaabbbaaabaa","abbbbababbbbaaa","bbabbbaababbab","a","bb","ababbaa","baaba","b","bbaabaabaa","abbaaabbbbabbaabaabb","aabbbbaaaa","aabbbbaaaaab","abbaaababbaaa","abaaaaaabbabbaa","baaaabaaabaaa","aaaabaabbabaababaab","aaabbbbaaaaabbb","babaabbbababbb","babbbb","bababaabbbbababaaba","aaaaa","baabbaabbbabb","baaabababbb","bbbabbaaaabaaabbbba","aaabbbabbaaababaa","babaaa","baabbabbbaabbaba","bbb","baabaababba","baabaaaabaaababababa","bbbbbaaabaaabaab","abba","baaaaaababbbb","bbabbbbbaaaaaababa","aaaaabbababbbba","abaabbbaabbabaabba","babbaabbaabbbbaa","aabbabba","abababababaabaabab","baab","baabaaaaaaaa","baaabababbbbbabba","bbaaabbaa","bbabba","bbbabbaab","baa","ab","baaaa","aaa","abbaabab","aabbbbbbaaaaa","aaaab","bbabaaab","bbaabaabababaaaaabb","aaaaaab","aabbbb","baaabbabaab","abaa","bbabbaabbabbbbbbb","aabbabbbabbab","abbbbbba","bbbbbaabaab","bbbbbaabbbbb","abbbbbbbabbbabb","aaaaaaababb","bababbbbbabbabb","aabababbabaaababaa","bababa","baabbabaabb","babbbbaabab","aabbbaaabbbbabaabb","abaabbbaaaaabababbab","abb","bbaab","abbaaa","abbbbaba","bbaabaa","bbbabbaabbaaa","bababab","baaaabbbb","abbbbaaaaaba","aaabaaabbaabaaabbaab","bababbaababb","aaaaab","aababbbbbababbbaab","aa","bbaaa","baaababaab","aabbaaabba","abbaabbaaaababbaaaaa","babaabaabbabbaaaaabb","bbabaabbaababaabbaaa","abbba","aaab","baabab","bbbbbbaabbaabbb","bbbabbabbaabbbabbab","bbabbabbbabbabbbba","abaabaabbabbabab","abbbbbaaababbbbbbbb","aaaaababbaaaaa","bbaababa","aabbbbbaba","baabababbbaba","aaabbbbba","aab","baaabbbbaabb","bbaaba","abaaaaaba","bba","bbabaaaab","abbabaaabba","abbabbb","baaabbaaabbbbbbaabb","aaababbb","aabbbbabaabaa","baaaaaaabab","baaaabbaaabbb","abbaaaabbbbbbb","bbaabbabbaabbaa","baababbbbabaababbaa","bbababbbbbab","baabbbabbbabab","aabaaabababaaa","bbbbaaabaaa","bbbabbabb","abababbaa","abbbbbbaababab","aabbbbabaa","abbabaabbaaababbbba","baabbabbbaaabbbbbbba","bbbb","aababbbabaabbaab","abbab","babb","aabaabbaabbababaa","aabbbbaaa","bbbab","baabbabbabab","baabbbabababba","abaaabbaababbabb","aababbaaabbbbbbbaaaa","aaabaabbbbbbbbaaa","baaabbbbaa","babaabaabbabaabbb","aaaabaaaba","bbababbbbbba","bbaaabaa","bbbaabbabaaaa","babbbab","abbaabbabababbbaa","bab","aabababbabbbbab","abbbabababb","baaabbaaab","babbbaab","baaabbbbbbbaab","abbbaaaaaab","aababbba","bbbababbbbaabaaabba","babbaabbb","bbaaabaabbb","baaabaabbbbbaa","baaaaaab","babbaabbbaabba","aabbbbaaabbabbbb","baaababaabbbabab","aaaabaab","baabbaaabbaaabb","aabaabaababbabaab","aabbaba","baaababbabbaaabbabb","aabaababaaaaabbbabaa","ababa","babbbbbbabaaabaabb","babbaaaabbbbaab","abbbabaababa","aabaaaaabbbbabab","aaabbbaabaaab","aababbaaaaaaaabbb","aaaabbababaab","aabababbabbbbbb","bbbbbabbbabbb","aabbaaaaaabbbba","abbabaababba","aaaaabbba","baaaaaaaabbbbbbbb","aaaabbbabb","abbbabaaa","aaabbabbabaabbaaa","bbaabaabbbbbbbbbaba","bbaaabbababaaba","baaabbaaaaaabbbbba","bbabbabbabbbbaab","aaabaaa","bababaaabaa","aabab","babbaba","aabbabbbaab","aaaabaaabbaaaabaa","bbaba","bbabbbaabbbbbabb","bbaabbaaaaabaab","ababbbaababbab","babaaab","babababba","abaaaaaaaaaab","aabbb","abababbbaabbaabaa","aaaabbaaabbbbaabaab","aababababbaababbb","babbaaaababaa","aabbabbaababbaaaba","aabbbabaababbab","abaaaab","babbbbbaaaababaaabba","bbbbababaabaaabaaba","aaabaabbbaabaabab","aaababbbaba","aabaaabba","aabbaabb","aaabbbabbabaaaabbbb","baabbbaabaabaabb","aaaabbbbababbabbabb","abbaabb","baaaabaaababababbba","aabababba","baaaaaabbbabbbbaa","babbab","aaabaaaaabbaaaaaba","aabbaaa","aaba","aababbababab","baabaabbaababbab","abaaaabba","bbaaaabbaabaaa","babbaaaabbbaaabaa","bbaaabbabaaa","abbabbaaabbabbbabba","aaabab","baaa","ba","bababbaab","aabaababb","bbabaaaaaaabbabb","aaaabbaaaaaabbbababb","aabbabbba","abbaaba","ababbaababbbbaaab","aabbabbaabba","aaaaabaabababbbabbb","bbaababbabaabbb","babbabaaaa","abbbbabaabb","bbaaaabaabbbbbb","abaaaaaaababbaaab","abbaaaabaaababba","ababbaabbaa","bbabaabbaaa","aababaaabab","ababaaabbabaabbbab","bbbaaa","aababbbabab","aaabaab","bbbbbbaaabbabbb","baaaabb","abaaabb","bbabbabbb","bbbbba","bbababaaababbbbaa","bbabaaba","bbaabaabaabbba","bbababaaabaaaba","bbbbbaabbaaaaaab","babaabaaaaaabaabaaab","baabbababa","bbaabbaaabbbbb","baabbaaabbabba","babbababaaaba","babbbbbbababbbabbbb","ababaabaaabbbb","aabbbaabaabbabb","bbabbababbabbabb","bbaabaaaabbbbb","bababba","aaaaababbbab","bbabbbaaababa","abbababbaabaabba","abaabaabbba","babbbbaaab","bbbbabbaababbabbbaab","ababaabababa","ababaaa","abbbaabaaaabaaaaab","aaaabbabbbaaaa","abaabaaaabbabb","bbbabaaab","bbaa","bbbaaababbabbbaabbbb","abbababbbbaabaaabb","babaa","bbababaaaababb","aaaaaabbbbbbbaabbb","bbbbabbab","aabbababa","babbbabbaab","bbbababababbbab","baaaabbaaaabbabbba","baaaaaa","abbbbaaaaaaaabbb","aabaaaab","aabb","bbaaab","abaabba","bbabbbbbaaaaabaaab","bbabbb","baabaaabbbbabaaabb","aaabababaabababbaaba","abab","babbabababbbabab","abbabbbbaabbaab","aaaabbbabaaba","babaaabababbaabaaabb","babaab","bbabbbbba","abbaabbbbaab","baaaaaaa","baaaab","bbbabaababbabaab","abaaaaaabababbab","aaaaaababbbaaaaabbb","baaaababaabaaabbbabb","abbaabbaabbb","bbaaaabbaabbaaabab","abaaaaba","abbbabbbabbaba","bbaabbabbabababbbaab","baabaabbbab","bbaabababbaaaaabaaa","aabaab","abbabab","bbabbbbbabb","baaabaaaabaabaaba","babba","aaaaaaabaaaaaabb","aabaa","aabaaabaaa","baaabaabbbbaabbaa","bbaabbbbbabbbababb","bbabbabaaa","bbabaaaabbaaaa","ababbb","aaabaaabbabaaaabaaaa","baba","aabbabbbaa","bbabaababbb","aaabb","aababaabababbbaba","bbabbbbbabba","baaabbbab","aaabbbbbbba","baabbbaababb","aabababa","aababaab","aabaaab","bbbabba","babaaabaaaaabbba","baabbaabbaabb","aaabaaababbbabaa","babaabaaabaaabba","bbbbabaaaaabbbab","aababaabaaaa","abaabbbbaababaaaabb","abbbabaa","abbbbbbbbbbbbbbbab","abbabbabbabbb","baaaabaab","bbabababababb","baabb","abbabaaabbabaaabbbaa","aaaabbababaaaabba","babaaaaa","abbabbbb","aabbaa","babaabbabbbabaabaaab","abbaaaa","baaab","bbbbbbbaba","babaabbabaaab","baaaabbbbbb","bbbbbbbaabbbbaaaaaa","bbbbabbba","aaababbbbaabaaaba","babbbbb","bbabab","baaabaabbbababb","baabbaaaaaaa","bbabaaaabbaa","baabbbbbaa","bbababbbbaabababa","aaabababb","bbaaaabbbbbabbbabab","aaabbbab","aaaaaaaaabbbbbaaaba","aaabaaabbababa","abaabbaabbabaabbab","aababbaaaaaaabbabb","aabbbbabba","bbababaaaaababbab","bbbbaaabbaa","aaaabaa","aaabaaaaaababbbba","bbbaaaaabbbbbabbabaa","baababaabaabbbb","abbbaaabaabaaab","aabaaabbbbaaabbaab","aabaabbaaaaaaaaaaa","baabababbb","bbbbbaabaaaabaababbb","abbaabbaba","babbbaaabbaab","baaaabaaa","aababbbaabba","bbbabaaa","aabbaaaaaaaaab","baaaaabbaaabaa","bababbbbabbaaaaa","bbbabbabaabaaaaabb","aaaaaaaaabbaababbb","aaaabb","bbbbaaabaabbbbaab","bbbaabbabbbbbbbbabb","abbaaaaaaaabba","abbaaaaaabbbbbb","aababbbbbaabaabbbb","aaaaababaabaab","baaababbabbba","bbbbbabaabbbaa","aaaaabaabbbbbbbab","aabbbbbb","abbb","bbbaaaabbababbabbb","bbabaabaabba","abaaabbbaaaabbb","ababbbbabbb","aaaabbbaaaaaabb","bbaabbbaaaaab","abbaabbabaab","babbba","abababbabbaabba","aabbababbbaabba","abbbabaabaabbbaa","baaaabbaaaa","baabaa","abaabbabbbaabbaaab","bbbbaabbbaabbbbab","abbbbbbaaabaababb","bbbaaababbaabb","bbaaabaabaabbbaaabb","babab","abbbbbbbbbbbbb","abaaba","bbabbababbbbbbaab","baabababbbb","abaababbabaa","aaaaaabbaab","babbbbbbbbbbbaaa","aabbba","babaaababbbbbbbaa","ababaaababbaba","bbaaababbbaababa","aaaabaaaaaaaab","bbababba","abaaababbb","bbabbabbbab","bbbbabbabb","babbabbaaabbbbaa","bbbbabaaaab","aaabbaaaabbb","baaabaab","aabaabbbbbaaba","baabbabaabba","abbbbaabababaabaaab","aabbabaab","aaabbbbb","bbbabbbbbabb","abbbb","baaababa","babababbbb","bbabbbbbaabbab","abbabaabaaaa","bbbaa","ababbbb","aabbbaab","aaabaaaabbbbaabab","abbbbbbabaabaababaaa","bbaabbba","babbababaaab","bbaabababbabbbbbbab","ababbbabbabaabaa","aabbaabbb","aaabbbbabaabaabb","babbaaaaaababb","abaaaabaaaabbaab","aaabaababaabbaabbaab","aaabbbbbbbbaabbbaab","aaababababaabaaa","aaabbababbaaaaaababb","baabbb","abaabaaaabb","abbabbaabaabbb","baaaaaabbbbbab","aabbabaabab","bbaaaaaaaaabaaaaaabb","abaabbbaaabaaababb","babbaaabbbb","bbabb","babaababbaaabbaaaba","babbbabaaaab","abaabbababababbaaaaa","abbaabaabababbb","aabbbabb","aabbbaabbbbaaaabba","babbabbbaaaababaabba","bbbbbbaabbabbbbabba","bababaaababbbababaa","bbaababbabaaaa","bbba","abababaabaababaabb","aabbbbabaababbab","abbaba","babaaaabbbababa","abbbaab","ababaaaaabbabbb","bbabbbbbabaabaabbbba","aababab","abaaaabbababbaab","bbaaabbbbabaab","aababbbaa","aababbbabbababbbbaba","baabaaaaaabab","bbbababbbbab","baaabbbaabaabbb","aaaaabababaaaaabb","abababbbaaaabbab","bbbabaa","abaaabbbabbaaaabbbbb","bbbbbbbab","bbbabbbbaababba","abbbabababab","abbbbbbbaaaaaabbabbb","aaaaaabaaabbbabab","abbaaaabbbababbbaa","bbbbbbaabbbaababaa","baabababababbbaaba","baaaaaabbabbaabbbaba","aaabaaabababbabaaaab","aababbababbabab","abaaababa","bbababaabbbabb","abbbababbb","bbabbabbaabab","aabbaabaabbbabb","bbbabab","baaaaabba","aaaabbabbbb","babbbaaaaa","babbaaa","baaababbaab","abaaabbaaaaabaab","abbbaaabaabaabaa","baababbbbaaaba","aaaaabbbbaababaa","babbbaabbbbabbbbabaa","bbaabaabbaabbbb","aaaaaabaaaaaaabbaa","abbbbbaaba","bbaaaaabbabaabba","aaabbbaababaaaabbbbb","bbabbababaaababaa","bbbabbaaabaaababaa","babbabbbb","abbbaabb","aabbbaabbbbbbaa","aabbbbbaabbbbaaaaba","baababbbbabbaa","abbabb","baabaaabbabbbabaa","aaaaababab","aaabbbbbbbbbb","bbaaaabbbabbbba","aaaabababab","abaaaabaaab","bababbbaa","abbbbbabaa","bababbababbabbbbb","aabbaaaa","abbbbbaab","aaaabbbaabbbab","aaabaaaabaa","ababbbbbbaababbabba","baabbabbaaba","abaabbaaab","aaabbaabbaabbaaaaba","baabba","aabbbaababbaaabaaaba","babaaaabbbab","aaaaabbbbbaaaa","bbbabbaabbb","bbbbaabbabbaababbbbb","baabbaa","aaaaba","aabaabaaababbbaa","bbaaaaabab","ababbababbabbaaa","ababbbaaaab","babbaababaaaabbabb","aabaaaabaabbabaaa","abbabaaabbabb","abbbbabbbbbb","babaabaa","bbabbaabbabb","baabbabbbaba","bbab","bbababaabb","bbabbaaabbaaa","ababbabbabaaaab","bbabababaaaabababb","baaababbbababbbbba","bbbaabaabbaabbaba","aabababbaaaba","bbbaaaabaabbaababaab","bbbaaaabbbabababa","bbaabab","baaabbaabbaaaababba","aaaabbbbbaaab","baabbbabbab","abbaaabaaab","baabaaa","bbbbb","aaaaabbabaaaaaabbbba","aaabbababbbaabbaaab","aababbaabaaabbbbaba","bbbbbbbaaaabbbbabbbb","abaabbabbaaa","baabaaaabbbabb","baabbaabbabbbbabbaba","aaabbabaa","bbaabb","babaaba","bbababaaaaaabbbaab","abababbba","bababbaaabbabbab","bbbbbaabab","bababbaababbaaababaa","bbbbaab","aaabababaa","abbaaaabbbaaab","aabbaaaabbaba","aaababbaababbbaabbbb","ababba","bbbababbabababba","abbbabaabbaabaab","aaabbba","bbbbababbaaaababa","aababababba","bbaabbbbabbaaa","aaaaaaabbbba","bbaabbbbabaaaaaaa","bababaaaabaab","aaaa","abbabaaabbbaabbb","baabbbabbaa","bbbabbbbaaabababaa","bababbbbbaaababb","bbbbbb","abbbbbbbaaabbaaab","abbbaaab","bbaaaababa","bbabaabbbababbbbbb","baabbbbbbaaabbab","abbbbbabbabaaaba","baabaabab","bbbababbbbbabaaaaaaa","abbaabbbbbabaaaab","abbbaabbabbabbbaab","bbbbbbabbbbaaaaab","abababababa","babaaaaaaaaaa","aababbbaabbb","abbabbbaaaabbbbbbbb","baaababbbbaaabaababa","baaabaabaababaaabba","bababbababbbaabb","abbabbaabba","babaabbaaaaabbb","abbabbbbab","abbbba","abababaaabaabbaa","bbbba","bbabbbbaaaabbbaaba","aabaabb","ababbbaabbbaaababba","bbaaabaaaaabaabbbaa","babaaabbaaaabbbba","aaaabaabbbabbbbaba","aaaabbaaaabab","aaaabbabbaabaabaaab","bbabbabbaaab","babbbbaaaaaabbba","aabbabb","bbbbaa","baabbbaabaaaa","aababbbaabaabab","aabbbbbababba","bbbbbbabbbbbb","babaabbbaaaaabbbaa","bbbabaabbaa","bbbbaaabaaaba","abbbaabaaaabab","aabbbabbb","aaaabaaabbabbbbbbbaa","bbabaaaababaabaaaab","aabaaaabaaabbbaabbab","baabbbbabba","bbbaaababbbbabbaaaaa","aabbbaaaaa","bbaaaa","bbbabaaababaaaababa","aaabbbbaaabbbabba","aabaaabab","abbaabaaaabbbab","abbababbbbabbab","aaabbaaaaaaaba","aaaabab","aaaababa","aabbbbbbbba","bbbbbbbbaabbabaabb","bbaababaaabbaabab","abaabb","bbabaab","aaabaabbbababbb","bababbaaaa","aabbbbaabbababababbb","baabaabaabaaaab","babbaabaaaa","bbbaaabaabbbaaaabb","bbaabbbb","aaaaaa","abbaabbbbbbaaaaba","abbaabaab","abbbabbaaaaabaa","babaabaaaabbab","bbaabbaaababababbabb","baaabaaaab","babaaabbabaabbaabb","bbbbaaba","abbbaa","aaaabaabbba","aabbbbbabaa","bababaaaaaabba","baaabbabaabb","bababbbaabbabb","bbaabbbaaba","aaabaa","bbababbb","abaabbbbaaabaa","bbbaabbbab","babababbbaabba","bbabaaaaabaaa","abbbbbbb","bbbabababa","babbbbbababbabbbbab","baabbabaabbbbbbababb","baabbabbbabbaaaaa","abbbaabaab","baabbaabbabbbaabbba","aaabbbbbb","abbabbabbbbaabbaaba","ababaabbbbbaaa","aaaaabbabaaaababb","aabababaaaabb","bbbaaababbbbabbaa","bbababbaaa","aabbbabbbabbbbb","babababbabab","aabbbabababbbabbaa","abaaaa","bbaaabaaabbbabb","baabbbbbbabbbbbbaab","babbabababaabbaabaaa","ababb","bbbaabbaabbabaaba","aaaaaabbbbabaaaab","bbbbabaababbababab","bbaabaababbbbbaaabb","abaababbab","bbbbaaabbbabaababba","bbbbaababbbaaa","abaaaabbbabbaa","babbaaaaabb","bbaaababbab","aabbabbbaabaaaaab","bababaa","aaaaaaaaa","ababababb","bbaababab","abbabbaaabbbb","abbbaaaa","abaabbbaba","abbbbabaabbababbbb","baababbbabaaaaa","baaababaaaaaba","abaaabaaaa","ababbbbaabbaaaaaa","babaaabbba","aababbbaaabbabaabab","ababbbbaba","aababaaabbaaab","aaaaaaabb","ababaabaabb","bababbbaabbabba","abaaaba","bbbbaaaabbababbbb","abaaabbabbaabba","abaabaabaaabbbaba","bababababbb","abbaaabaaaabaaaabaaa","abbbababa","bbaabbaaaaaaaabbbbba","abbaaabbba","bbabbabbbaa","baababaaabaaaba","baabbaaabbabaaaabab","bababbabbbaaaabbaba","aaabaaba","aabbab","baababbbb","babbbbbabbabaa","aababaabaabbaabba","babaaabbbb","aaaabbaaabbabb","abaabaaaaababba","aaaababbabbbaaba","abaaabbaabbb","aabbbbbaabbaab","bbabbaa","abaaababbbbbbbaaabaa","aaaaabababaabaa","aabbbbaababaaabaaba","bbababaabbabbaaabbbb","aabaaaabbaaba","bbaabbabbbaaaab","baabaabbbbbbbbbaab","bbaaabbbbaabaaaa","abbbbbbabbababb","aababbbabbbbaa","bbaaaaa","ababbbaaababbababb","abaabbaabbabbb","aabbaab","aababbabaaabbbbab","baaaababaaab","babbbbbbabbab","abbbbbabaaababbaa","babbbaaaba","baabbbaaab","abababaaaabbbbbaab","bababababaa","bbabbaabbbbaaa","bbbabbab","aaaaaabbab","bbabaababaabbb","aaaaaaabbababbaabba","abbabaaaaaab","aabaaaa","abbaabbb","abaaabaabaaa","aababbbbbbaabaabbabb","bbbaaaaaabbab","aabbbbabababb","baabaaaabbabaabb","aaaaabbb","abbabbbbbba","bbbbbabbaaaabaabaaa","ababbaaaababaa","baaabab","aabbababbaababbb","baabbabbaaaaaa","babbbabbbaabbaba","aaabaabababaababa","babaabbaaaba","aaabbbabaaaaa","abbaaaabaabbbaa","bbaabbababbaaabb","aaaaabababaa","bbaabbababbbbb","abbbabbbbabaaaba","bbbaababaabaaaabaaaa","bbaaaababbbbba","abbbabaaabb","aababbbbabbaaa","abababaaaabbab","bbbbbbbbaaaaaaaa","aaaabbaaaabbbaabbb","aaaabababb","abbbbbabab","ababbbaaaaababaaaaab","babaaaa","babbabbbbbbbb","bbbabbaaabbbbbbba","abbbabbbaaaaaabbb","bbaabbbbbbbababab","bbabaaabbbbb","aaaaaabb","aaaabaaabbba","abbbaaababbaababaaab","aaaababaabbabbaab","aaababbbbbabbbabbba","aabababbbbbbbaababa","ababaabbabbbbabba","aabbabbabaaa","bbbababb","aabbaaabbabaaa","abaabbaabbbbbababb","aaaaababbaaabbaaaaba","bbbbaabaaabaaababb","bbbaba","abbabbbaabbabbbbaba","aaaababbaaaaabb","aabbbbababaabbbbaab","abbababba","abbbaaabaabbbabaaaab","bbbbbaabaaabaabb","aabbaabbaaaaabaaaaaa","abbabaaaaaaaba","bbababbbbbababaab","bbabababa","babbababaababbabbb","bbbbbbba","bbababbabbbabbabbaba","bbbbbaabbbabaaba","aaaababbababbabaabaa","bababaabbba","ababbbbbabbbaaa","abbbabbaaab","bbbabaaaa","bbbabbb","baaababbabaaabbaaba","bbbabaabbaaaabb","aabbbabaabaaabb","aabbabbbabbbabaa","bbbaaba","aabbabaabbababbaa","bbaabbabbab","bbaabaaaaabaabbaaaab","abbabbabbabbaba","abbabbbabaababbb","baabbbaabaa","aababaabaabbaaabb","babbbababbabbaab","aaabbaaaaabaab","aaaabbbabaaabaabaaa","bbabbbbbba","ababbbbaabaaaaaaaa","babbbbbbbbaab","bbbbbaabaaba","aababaaaabaaaaaba","babaaabababbaabbaabb","ababbabbaaabbbabbbaa","aabaaaaabba","bbbbabbabbababbb","ababaababbbbaaa","bbbbbbaaabaaa","babbabbbababaaaabbbb","bbabbbbb","abaaabbababbaaabbb","bbbaaabaaab","bbabaabbaba","bbbbababbbbbbbbab","baaaaaaaaabbabababab","babbbbabbaaabb","bbbaabb","babbaa","aabbabbaabbb","aabba","bbabbbbaabbbbbb","aababbbbbababbaabb","aaaabbbababbaaaaaaba","babbaabaaabbaaa"]))



