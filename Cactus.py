
# xx   xxxx
#X--X X/---X
#X--X X//--X
#X--X X///-X
# xxxxX~~~~X  xx
#     X---\X X--X
#     X--\\X X--X
#     X-\\\X X--X
#     X~~~~Xxxxx
#     X~~~~X
#     X~~~~X
#     X~~~~X
#     X~~~~X

# xx(scale)(scale+1)  xxxx(scale*2)
#X--X X/---X
#X--X X//--X
#X--X X///-X
# xxxxX~~~~X  xx
#     X---\X X--X
#     X--\\X X--X
#     X-\\\X X--X
#     X~~~~Xxxxx
#     X~~~~X
#     X~~~~X
#     X~~~~X
#     X~~~~X
#top cactus
#middle cactus
#bottom cactus


scale = 2

def main():
    draw_upper_cactus()
    draw_middle_cactus()
    draw_lower_cactus()

def squiggle():
    print('X' + ('~' * (scale * 2)) + 'X')
# xx   xxxx
#X--X X/---X
#X--X X//--X
#X--X X///-X
def draw_upper_cactus():

    print(' ', end='')
    print('x' * scale, end='')
    print(' ' * (scale + 1), end='')
    print('x' * (scale * 2))
    for i in range (1, scale * 2):
        # Left Arm
        print('X', end='')
        print('-' * (scale), end='')
        print('X', end='')
        # Space
        print(' ' * (scale - 1), end='')
        # Middle Stem
        print('X', end='')
        print('/' * (i), end='')
        print('-' * ((scale * 2)- i), end='')
        print('X')

# xxxxX~~~~X  xx
#     X---\X X--X
#     X--\\X X--X
#     X-\\\X X--X
def draw_middle_cactus():
    #Draw Xs
    print(' ' + 'x' * (scale * 2), end='')
    #Floopy
    print('X', end = '')
    print('~' * (scale * 2) + 'X', end = '')
    print(' ' * scale + 'x' * scale)
    #Stem + Right arm
    for k in range (1, scale * 2):
        #Stem
        print(' ' * (scale * 2 + 1) , end = '')
        print('X', end = '')
        print('-' * (scale * 2 - k), end = '')
        print('\\' * k, end= '')
        print('X', end = '')
        #Right Arm
        print((' ' * (scale - 1 )) + ('X' + ('-' * scale )) + 'X')
    

#     X~~~~Xxxxx
#     X~~~~X
#     X~~~~X
#     X~~~~X
#     X~~~~X
def draw_lower_cactus():
    print(' ' * (scale * 2 + 1), end='')
    print('X', end = '')
    print('~' * (scale * 2) + 'X', end = '')
    print('x' * (scale*2))
    for l in range (scale * 2):
        print(' ' * (scale * 2 + 1), end='')
        squiggle()
              

main()

