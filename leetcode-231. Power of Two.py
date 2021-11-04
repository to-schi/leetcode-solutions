class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n >= 1:
            n = n / 2
            if n == 0.5:
                return True
        return False
    print(isPowerOfTwo(1, 128))

# with count:
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         count = 1
#         if n == 1:
#             return True, count-1
#         elif n == 2:
#             return True, count
#         else:
#             while n > 1:
#                 n = n / 2
#                 count = count+1
#                 if n == 2 or n == 1:
#                     return True, count
#             return False
#     print(isPowerOfTwo(1, 8))
