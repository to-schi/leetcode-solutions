def intToRoman(self, num: int) -> str:
#    dec = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'} no
     decimal = list(num)

     reverse(list) 
     list_rev[0] = einer
     list_rev[1] = zehner
     list_rev[2] = hunderter
     list_rev[3] = tausender


print(intToRoman(1,1564))



def romanToInt(self, s: str) -> int:
        rom = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        dec = rom[s[-1]]
        for i in reversed(range(len(s)-1)):
            if rom[s[i]] < rom[s[i+1]]: # wenn value zu key s[i] in Roman (z.B. Key I : Value 1) ist kleiner als das danach, dann - value (1)
                dec -= rom[s[i]]
            else:
                dec += rom[s[i]]
        return dec
print(romanToInt(1,"MDLXIV"))