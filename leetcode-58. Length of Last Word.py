def lengthOfLastWord(self, s: str) -> int:
    sentence = s.split()
    return len(sentence[-1])

print(lengthOfLastWord(1, " moon  "))
# working!
