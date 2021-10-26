
def hasAlternatingBits(self, n: int) -> bool:
    if n <= 1:
        return True
    b = bin(n)[2:]
    print(b)
    return (all(b[i]!=b[i+1] for i in range(0, len(b)-1)))    # all() iterations must be True!

print("5: ", hasAlternatingBits(1, 5))
print("6: ", hasAlternatingBits(1, 6))
print("10: ", hasAlternatingBits(1, 10))
print("11: ", hasAlternatingBits(1, 11))
# working!
