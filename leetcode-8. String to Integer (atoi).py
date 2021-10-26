def myAtoi(self, s: str) -> int:
        string = s.lstrip()
        r = list(string)
        digits = ['-','+','1','2','3','4','5','6','7','8','9','0']
        #num = []
        for char in reversed(r):
            if char not in digits:
                r.remove(char)
        for i in range(0, len(r)):
            if r[i] == "-" or r[i] == "+":
                del r[:i]

        print(r)

print(myAtoi(1, "00000-42a1234m"))
#         for char in res[0:len(s)]:
#             if char not in digits:
#                 return 0

#             if char in digits:
#                 num.append(char)
#             else:
#                 break
#         if len(num) == 0:
#             return 0
#         elif len(num) == 1 and num[0] == "-" or len(num) == 1 and num[0] == "+":
#             return 0
#         elif num[0] in ["+", "-"] and num[1] in ["+", "-"]:
#             return 0
#         if int("".join(num)) > 2**31-1:
#             return 2**31-1
#         elif int("".join(num)) < -2**31:
#             return -2**31
#         else:
#             return int("".join(num))


# print(-2**31)
# not accepted 0000000-42koig


# Input: s = "4193 with words"
# Output: 4193
# Explanation:
# Step 1: "4193 with words" (no characters read because there is no leading whitespace)
# ^
# Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
# ^
# Step 3: "4193 with words" ("4193" is read in
#                            reading stops because the next character is a non-digit)
# ^
# The parsed integer is 4193.
# Since 4193 is in the range[-231, 231 - 1], the final result is 4193.
