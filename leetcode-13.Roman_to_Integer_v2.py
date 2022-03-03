'''Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000'''

roman = input("Type in a roman number: ")
# MDCLXVI = 16666; MCDXLIV = 1444
def romanToInt(self, s: str) -> int:
        rom = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        dec = rom[s[-1]]
        for i in reversed(range(len(s)-1)):
            if rom[s[i]] < rom[s[i+1]]: # if value of key s[i] in Roman (e.g. Key I : Value 1) is smaller than the next: value (1)
                dec -= rom[s[i]]
            else:
                dec += rom[s[i]]
        return dec

print(romanToInt(1,roman))
# working!
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
