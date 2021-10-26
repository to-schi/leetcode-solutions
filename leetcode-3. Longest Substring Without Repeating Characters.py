def lengthOfLongestSubstring(self, s: str) -> int:
    map = []
    out = []
    for char in s:
        map.append(char)
    l = 0    
    r = 1
    while l < r < len(s):
        for char in map:
            counts = map.count(char)
            if counts <= 1:
                out = s[l:r+1]
                r += 1
            else:
                l+=1
                r+=1
    #print(len(set(s[l:r+1])))
    return out
print(lengthOfLongestSubstring(1, "bbdsfgbbbb"))
# not working
