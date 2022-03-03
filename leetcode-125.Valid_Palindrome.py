'''
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
https://leetcode.com/problems/valid-palindrome/
'''

def isPalindrome(self, s: str) -> bool:
    #alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    string = s.lower()
    pal = []
    for i in range(0, len(string)):
        if string[i].isalnum():
            pal.append(string[i])
    print(pal)
    if pal == pal[::-1]:
        return True
    else:
        return False
print(isPalindrome(1, "A man, a plan, a canal: Panama"))
