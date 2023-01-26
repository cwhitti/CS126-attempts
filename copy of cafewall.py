from turtle import *
from Lab2_functions import *

MORTAR = 2

#our turtle
shape('turtle')
color('black')
width('2')
speed(99999)

#our environment
setworldcoordinates (0,400,650,0)
bgcolor('gray')



#1
def Q1(repeat,x,y,x_size,stack,offset):
    #stack the boxes
    for loop in range(stack):
        #draw the boxes
        
        for length in range(repeat):
            draw_rect(x,y,x_size,x_size,'black')
            x+= x_size
            draw_rect(x,y,x_size,x_size,'white')
            x += x_size
        #Move to the front of the boxes
        x = x - (x_size * (repeat * 2))
        up()
        goto(x,y)
        down()
        #draw the blue line on black boxes
        for line in range(repeat):
            draw_line(x, y, x + x_size, y + x_size, 'blue')
            draw_line(x, y + x_size, x + x_size, y, 'blue')
            x += x_size*2
        x = x - (x_size * (repeat*2))
        # empty line
        y += x_size + MORTAR        
        
def rows():
    for offsets in range(stack):
        print(Q1(repeat,x,y,x_size,stack,offset))
        x += offset
        print(Q1(repeat,x,y,x_size,stack,offset))
        x -= offset


    
def main():
    shape('turtle')
    color('black')
    width('2')
    speed(99999)
    rows(Q1(4,0,0,20,1,0))
    rows(Q1(5,50,70,30,1,0))
    rows(Q1(4,10,150,25,8,0))
    rows(Q1(3,250,200,25,6,10))

main()
