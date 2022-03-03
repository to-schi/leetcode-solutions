'''Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000'''
def romanToInt(self, s: str) -> int:
    integer = 0
    for i in range(0,len(s)):
        if s[i] == "I":
            if i == (len(s)-1) or s[i+1] != "V" and s[i+1] != "X":
                integer += 1
            else:    
                integer -= 1
        elif s[i] == "V":
                integer += 5
        elif s[i] == "X":
            if i == (len(s)-1) or s[i+1] != "L" and s[i+1] != "C":
                integer += 10
            else:    
                integer -= 10
        elif s[i] == "L":
            integer += 50
        elif s[i] == "C":
            if i == (len(s)-1) or s[i+1] != "D" and s[i+1] != "M":
                integer += 100
            else:    
                integer -= 100
        elif s[i] == "D":
            integer += 500
        elif s[i] == "M":
            integer += 1000
    return integer
print(romanToInt(1,"MDLIV"))
# working!
#   I can be placed before V (5) and X (10) to make 4 and 9. 
#   X can be placed before L (50) and C (100) to make 40 and 90. 
#   C can be placed before D (500) and M (1000) to make 400 and 900.
