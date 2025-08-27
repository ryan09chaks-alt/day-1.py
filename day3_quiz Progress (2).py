import turtle
from turtle import *

pen = turtle.Turtle()
pen.pensize(2)
pen.speed(0)

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=640, height=640)

side_length = 20

# Start position
pen.penup()
pen.goto(-320, 320)
pen.pendown()

# Ask for initial color
pen.fillcolor(input("Enter the color you want the turtle to fill with: "))

# Draw a single square
def draw_square():
    pen.begin_fill()
    for _ in range(4):
        pen.forward(side_length)
        pen.right(90)
    pen.end_fill()
    pen.forward(side_length)  # move to next square position

# Draw multiple squares
def draw_multiple_squares(count):
    for _ in range(count):
        draw_square()

# Move to a new line
def reset_line():
    pen.penup()
    pen.right(90)
    pen.forward(side_length)
    pen.left(90)
    pen.goto(-320, pen.ycor())  # go back to start of line
    pen.pendown()

# Create a line of squares and change color
def create_line_of_squares():
    color_input = input("Enter the new color you want the turtle to fill with: ")
    pen.fillcolor(color_input)
    num_input = int(input("Enter the number of squares you want to draw in this line (max 32): "))
    draw_multiple_squares(num_input)

# Main loop
while True:
    direction_input = input("Enter the direction you want the turtle to move: ")
    if direction_input.lower() == "exit":
        break
    elif direction_input.lower() == "c":
        create_line_of_squares()
    elif direction_input.lower() == "s":
        num_squares = int(input("How many squares do you want to draw? "))
        draw_multiple_squares(num_squares)
    elif direction_input.lower() == "n":
        reset_line()
    else:
        print("Invalid input. Please enter 'c' to change color, 's' to draw squares, 'n' to move to a new line, or 'exit' to quit.")

turtle.done()

