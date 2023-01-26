def mystery(b, c):
    return c + 2 * b

def main():
    a = 4
    b = 2
    c = 5

    a = mystery(c, b)
    c = mystery(b, a)
    print(a)
    print(b)
    print(c)

main()
