def surprise(y, x):
    x += 1
    print(x, y)
    y -= 1
    return x
​
def main():
    x = 5
    y = 1
    z = 9
    w = y + 2
​
    surprise(x, y)
    x = surprise(z, w)
    w += 1
    z = surprise(w, x)
    surprise(y, z)
​
main()
