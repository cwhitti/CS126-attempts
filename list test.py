mylist = []


def main():
    results()

def results():
    color = test1()
    movie = test2()
    drink = test3()

    print(f"Your favorite color is {color}")
    print(f"Your favorite movie is is {movie[1]}")
    print(f"Your favorite drink is {drink}")

def test1():
    color = input("What is your favorite color? ")
    return color

def test2():
    food = input("What is your favorite food? ")
    movie = input("What is your favorite movie? ")
    return food, movie

def test3():
    drink = input("What is your favorite drink? ")
    return drink

main()
