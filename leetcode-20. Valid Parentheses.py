
def isValid(self, s: str) -> bool:
    brO = []
    brC = []
    sqO = []
    sqC = []
    cuO = []
    cuC = []
    for i in range(0, len(s)):
        if s[i] == "(":
            brO.append(i)
        elif s[i] == "[":
            sqO.append(i)
        elif s[i] == "{":
            cuO.append(i)
    print("brO: ", brO)
    print("sqO: ", sqO)
    print("cuO: ", cuO)
    for i in reversed(range(0, len(s))):
        if s[i] == ")":
            brC.append(i)
        elif s[i] == "]":
            sqC.append(i)
        elif s[i] == "}":
            cuC.append(i)
    print("brC: ", brC)
    print("sqC: ", sqC)
    print("cuC: ", cuC)

    if sum(brO) < sum(brC) and len(brO) == len(brC):
        a = 1
    elif len(brO) == len(brC) == 0 :
        a = 1
    else:
        a = 0
    if sum(sqO) < sum(sqC) and len(sqO) == len(sqC):
        b = 1
    elif len(sqO) == len(sqC) == 0:
        b = 1
    else:
        b = 0
    if sum(cuO) < sum(cuC) and len(cuO) == len(cuC):
        c = 1
    elif len(cuO) == len(cuC) == 0:
        c = 1
    else:
        c = 0
    print(a, b, c)
    if a == b == c == 1:
        return True
    else:
        return False

print(isValid(1, "([)]"))
#                 01234567
#                   2  5
#                  1    6





    # if len(brO) != len(brC):
    #     a = 0
    # elif len(brO) == 0:
    #     b = 1
    # else:
    #     for n in range(len(brO)):
    #         if brO[n] < brC[n]:
    #             a = 1
    #         else:
    #             a = 0
    # if len(sqO) != len(sqC):
    #     b = 0
    # elif len(sqO) == 0:
    #     b = 1
    # else:
    #     for n in range(len(sqO)):
    #         if sqO[n] < sqC[n]:
    #             b = 1
    #         else:
    #             b = 0
    # if len(cuO) != len(cuC):
    #     c = 0
    # elif len(cuO) == 0:
    #     c = 1
    # else:
    #     for n in range(len(cuO)):
    #         if cuO[n] < cuC[n]:
    #             c = 1
    #         else:
    #             c = 0   
    # print(a, b, c)
    # if a == b == c == 1:
    #     return True
    # else:
    #     return False    

#                 0123456789
#                 0   4  
#                  1   5
#s.find(")") > s.find("(") and s.count("(") == s.count(")")
#     if s[i] == "(" and s.find(")") > s.find("(") and s.count("(") == s.count(")"):

# for i in range(0, len(s)):
#     if s[i] == "[" and s.find("]") > s.find("[") and s.count("[") == s.count("]"):
#         print(i)
#         return True

# for i in range(0, len(s)):
#     if s[i] == "{" and s.find("}") > s.find("{") and s.count("{") == s.count("}"):
#         return True
