def addBinary(self, a: str, b: str) -> str:
     sum = (int(a, 2)+int(b, 2))
     return format(int(a, 2)+int(b, 2), "0b")

print(addBinary(1, "0", "1011"))
