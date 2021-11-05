import collections
from typing import Collection

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return collections.Counter(s) == collections.Counter(t) reicht!!!!!
        # or return Counter(s) == Counter(t)
        if len(s) != len(t):
            return False
        else:
            rem = list(t)
            for c in s:
                if c in rem:
                    rem.remove(c)
                    if len(rem) == 0:
                        return True
                else:
                    return False

    print(isAnagram(1, "rac", "car" ))

# working!





# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         d = dict.fromkeys(s, 0)
#         for ss, tt in zip(s, t):
#             if tt not in d:
#                 break
#             d[ss] += 1
#             d[tt] -= 1
#         else:
#             return not any(d.values())
#         return False


