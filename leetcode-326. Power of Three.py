class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        else:
            while n >= 1:
                n = n / 3
                if n == 1:
                    return True
            return False

    print(isPowerOfThree(1, 9))


