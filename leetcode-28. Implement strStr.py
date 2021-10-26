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


for i in range(0, int(n/2)):
    if Wort[i] != Wort[n-1-i]:
