import numpy as np
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 0: return False
        else:
            ternary = np.base_repr(n, base=3)
            print(ternary)
            if 1 == sum(int(x) for x in ternary):
                return True
            else:
                return False
#working
    print(isPowerOfThree(1, 9))
