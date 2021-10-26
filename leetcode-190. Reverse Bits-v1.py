def reverseBits(self, n: int) -> int:
    b = format(n, "032b")
    b_rev = b[::-1]
    dec = int(b_rev, 2)
    return dec
print(reverseBits(1, 43261596))
#input must be str!!!!!

#b = bin(n).replace('0b', '')
# "{:032b}".format(n)

# 0b0000000000000000010110

#print('{:08b}'.format(i))
#print(format(i, "08b"))

#def decimalToBinary(n):
#   return bin(n).replace("0b", "")
#print(decimalToBinary(i))
