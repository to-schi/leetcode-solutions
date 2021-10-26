def fib(self, n: int) -> int:
    f = list((0, 1))
    for x in range(1, n):
        f.append(f[-1] + f[-2])
    else:
        return f[-1]

print(fib(1, 496))

