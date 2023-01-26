from turtle import *
from math import sqrt

#our turtle
shape('turtle')
color('white')
width('2')

#our environment
setworldcoordinates (0,400,400,0)
bgcolor('gray')

#Main
def main():
    test_square()

#Test square
def test_square():
    fillcolor('black')
    begin_fill()
    for box in range(4):
        forward(20)
        left(90)
    end_fill()
        
main()
