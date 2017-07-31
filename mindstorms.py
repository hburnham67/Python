import turtle
        
def draw_square():           
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(2)
    i=0
    while(i < 4):
        brad.forward(100)
        brad.right(90)
        i = i + 1

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    kyle = turtle.Turtle()
    kyle.shape("turtle")
    kyle.color("gray")
    kyle.speed(2)
    i=0
    while(i < 3):
        kyle.forward(100)
        kyle.left(120)
        i = i + 1

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("red")

    draw_square()
    draw_circle()
    draw_triangle()

    window.exitonclick()
draw_shape()
