class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        counter = 0
        remain = dividend
        if dividend < 0 and divisor > 0:
            return 0
        elif dividend < 0 and divisor < 0:
            while remain <= divisor:
                counter += 1
                remain -= divisor
            if counter % 2 == 0: #mod verboten!
                counter -= 1
            return counter
        elif divisor < 0:
            remain = -1*remain
            while remain <= divisor:
                counter += 1
                remain -= divisor
            if counter % 2 != 0:
                counter -= 1
            return counter
        else:
            while remain >= divisor:
                counter += 1
                remain -= divisor
            return counter
    print(divide(1, -10, -5))
-10, 3 => -3
negatives Ergebnis ist möglich


# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to - 2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than - 231, then return -231.

