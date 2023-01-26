from turtle import *

MORTAR = 2

#main
def main():
    setworldcoordinates (0,400,650,0)
    bgcolor('gray')
    shape('turtle')
    color('black')
    width('2')
    speed(9999)
    #box_line(x1,y1,size,repeat,stack,offset)
    standard_box_line(0,0,20,4,1,0)
    standard_box_line(50,70,30,4,1,0)
    standard_box_line(10,150,25,4,8,0)
    offset_box_line(250,200,25,3,6,10)
    offset_box_line(425,180,20,5,10,10)
    offset_box_line(400,20,35,2,4,35)
    

#---FOUNDATIONS---#
    
#*** this is my ROW for #1 ***
def box_line(x,y,size,repeat,stack,offset):
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
    #update x and y for new stack    
    x -= size * (repeat * 2)
    y += size + MORTAR
    up()
    goto(x,y)
    down()

def line(x,y,size):
    pensize(1)
    pencolor('Blue')
    up()
    goto(x,y)
    down()
    goto(x + size, y + size)
    up()
    goto(x, y+ size)
    down()
    goto(x + size, y)

#---FUNTIONS---#

#*** this is my GRID for #2 ***
def standard_box_line(x,y,size,repeat,stack,offset):
    for loop in range(stack):
            box_line(x,y,size,repeat,stack,offset)
            #update x and y for new stack    
            y += size + MORTAR
            up()
            goto(x,y)
            down()
            
#*** this is my OFFSET for #2 ***
def offset_box_line(x,y,size,repeat,stack,offset):
    for loop in range(1,stack+1,2):
        box_line(x,y,size,repeat,stack,offset)
        #update x and y for new offset stack
        y += size + MORTAR
        x += offset
        #update x and y for new stack, no offset
        box_line(x,y,size,repeat,stack,offset)
        y+= size + MORTAR
        x -= offset

main()
