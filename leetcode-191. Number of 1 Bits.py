def hammingWeight(self, n: int) -> int:
    b = str(bin(n))
    weight = b.count('1')
    return weight

print(hammingWeight(1, 3))
# working!
