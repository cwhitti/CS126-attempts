
# Header : A program that programatically prints a cactus based off of a
#          constant


# Constant
scale = 1

# Define Main
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
    print(' ' + ('x' * scale) + (' ' * (scale + 1)) + ('x' * (scale * 2)))
    for line in range (1, scale * 2):
        # Left Arm
        print('X' + ('-' * scale) + 'X', end='')
        # Space
        print(' ' * (scale - 1), end='')
        # Middle Stem
        print('X' + ('/' * (line)) + ('-' * ((scale * 2)- line)) + 'X')

# xxxxX~~~~X  xx
#     X---\X X--X
#     X--\\X X--X
#     X-\\\X X--X
def draw_middle_cactus():
    #Draw Xs
    print(' ' + 'x' * (scale * 2), end='')
    #Floopy
    print('X' + ('~' * (scale * 2)) + 'X' + (' ' * scale) + ('x' * scale))
    #Stem + Right arm
    for line in range (1, scale * 2):
        #Stem
        print(' ' * (scale * 2 + 1) + 'X' + ('-' * (scale * 2 - line)) + ('\\' * line) + 'X', end='')
        #Right Arm
        print((' ' * (scale - 1 )) + ('X' + ('-' * scale )) + 'X')
    
#     X~~~~Xxxxx
#     X~~~~X
#     X~~~~X
#     X~~~~X
#     X~~~~X
def draw_lower_cactus():
    #Floopy + Xs
    print(' ' * (scale * 2 + 1) + 'X' + ('~' * (scale * 2)) + 'X' + ('x' * (scale*2)))
    #Bottom Stem
    for line in range (scale * 2):
        print(' ' * (scale * 2 + 1), end='')
        squiggle()
              
main()

