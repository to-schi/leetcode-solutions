class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        return x_str == x_str[::-1]
 
    ans = isPalindrome(1,24542) # example (self, x)
    if ans:
        print("Yes")
    else:
        print("No")
# working!


