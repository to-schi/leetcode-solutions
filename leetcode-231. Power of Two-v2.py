class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
    # count all 1s in binary format
        if n > 0 and bin(n).count("1") == 1:
            return True
        else:
            return False
    print(isPowerOfTwo(1, -16))


