import turtle
import keyboard

#Make the turtle

turty = turtle.Turtle()
turty.shape('Turtle')
turty.setworldcoordinates(0,400,400,0)

#The game is currently playing
is_playing = True

#While the user has not quit the game

while is_playing == True:

    #If w is pressed, head upwards
    if keyboard.is_pressed('w'):
        turty.setheading(270)
        
    #If a is pressed, head left
    if keyboard.is_pressed('s'):
        turty.setheading(180)

    #If s is pressed, head downwards
    if keyboard.is_pressed('s'):
        turty.setheading(90)
        
    #If d is pressed, head right
    if keyboard.is_pressed('d'):
        turty.setheading(0)

    #if q is pressed, quit the program
    if keyboard.is_pressed('q'):
        is_playing = false
        
    turty.forward(1)
