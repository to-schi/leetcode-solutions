def reverse(self, x: int) -> int:
    if x < 0:
        x_str = str(abs(x)) # or (-1*x)
        x_rev = x_str[::-1]
        if -1*int(x_rev) >= -2**31:
            return -1*int(x_rev)
        else:
            return 0
    else:
        x_str = str(x)
        x_rev = x_str[::-1]
        if int(x_rev) <= 2**31-1:
            return int(x_rev)
        else:
            return 0
print(reverse(1, -8463847412))
# working!
#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#print(-2**31)
#print(2**31-1)
#> -2147483648
#> 2147483647
#Example 2: !!!!!
#Input: x = -123
#Output: -321

