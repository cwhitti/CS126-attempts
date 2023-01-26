def Fun(x):
    y = 0
    i = 0
    print("I'm thinking of a number between 1 and 100...")
    while y != x:
        y = int(input('Your guess? '))
        if y > x:
            print('It\'s lower.')
        elif y < x:
            print('It\'s higher.')
        i += 1
    if i == 1:
        print('You got it right in',i,'guess!')
    else:
        print('You got it right in',i,'guesses!')
    return i

from random import *
def Game():
    i = 0
    it = 0
    bi = 0
    g = 0
    p = True
    while p == True:
        x = randint(1,100)
        g += 1
        i = Fun(x)
        it += i
        if g == 1 or i < bi:
            bi = i
        ps = input('Do you want to play again? ')
        print()
        if ps[0] == 'y' or ps[0] == 'Y':
            p = True
        else:
            p = False
    return g,it,bi

def main():
    print('This program allows you to guess random numbers.')
    print('I will think of a number between 1 and 100')
    print('and you will try to guess it.')
    print('After each guess, I will give you a clue about')
    print('whether the correct number is higher or lower.')
    print()
    g, it, bi = Game()
    print('Overall results:')
    print('Total games   =',g)
    print('Total guesses =',it)
    print('Guesses/game  =',str(round((it/g),1)))
    print('Best game     =',bi)


main()


