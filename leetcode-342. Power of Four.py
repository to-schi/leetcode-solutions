import numpy as np


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False
        else:
            base_four = np.base_repr(n, base=4)
            print(base_four)
            if 1 == sum(int(x) for x in base_four):
                return True
            else:
                return False
    print(isPowerOfFour(1, 4))
