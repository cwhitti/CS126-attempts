def mystery(n):
    if (n < 0):
        n = n * 3
        return n
    else:
        n = n + 3
    if (n % 2 == 1):
        n = n + n % 10
    return n

print(mystery(-5))

print(mystery(0))

print(mystery(7))

print(mystery(18))

print(mystery(49))
