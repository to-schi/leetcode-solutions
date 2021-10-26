def reverseBits(self, n: int) -> int:
    b = int(bin(n)[2:].zfill(32)[::-1], 2) 
    return b

print(reverseBits(1, 43261596))
# make int on base 2 from binary of "n" without "0b" in front and filled with 0s + reversed [::-1]
# .zfill(x) fills with Zeros on the left to width of x 