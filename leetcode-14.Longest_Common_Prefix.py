'''Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".'''

def longestCommonPrefix(self, strs) -> str:
    #if len(strs) == 1:
     #   return(strs[0])
    pre = strs[0]
    for word in strs[1:]:
        while pre != word[0:len(pre)]:
            pre = pre[0:(len(pre)-1)]
            #plen -= 1
            if len(pre) == 0:
                return ""
    return pre

print(longestCommonPrefix(1, ["flight"]))
# working!
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
