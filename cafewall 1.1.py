from turtle import *

MORTAR = 2


def main():
    setworldcoordinates (0,400,650,0)
    bgcolor('gray')
    shape('turtle')
    color('black')
    width('2')
    speed(9999)
    #row(x1,y1,size,repeat,stack,offset)
    box(0,0,20,4,1,0)
    #box(50,70,30,4,1,0)
    #box(10,150,25,4,8,0)
    #row(250,200,25,3,5,10)
    #row(425,180,20,5,4,10)
    #box(400,20,35,2,10,35)

def box(x,y,size,repeat,stack,offset):
    for length in range(repeat):
        #black box
        up()
        goto(x,y)
        down()
        pencolor('black')
        fillcolor('black')
        begin_fill()
        for black_box in range(4):
            forward(size)
            left(90)
        end_fill()
        #draw line
        line(x,y,size)
        ##update X for new X position
        x += size
        #white box
        pencolor('white')
        fillcolor('white')
        begin_fill()
        for white_box in range(4):
            forward(size)
            left(90)
        end_fill()
        #move [size] units to the right
        x += size
        up()
        goto(x,y)
        down()

def line(x,y,size):
    pencolor('Blue')
    up()
    goto(x,y)
    down()
    goto(x + size, y + size)
    up()
    goto(x, y+ size)
    down()
    goto(x + size, y)

main()
