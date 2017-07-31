import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("white")
    
    flower = turtle.Turtle()
    flower.speed(100)
    flower.shape("turtle")
    flower.right(45)
    for i in range(1,37):
        for j in range (1,3):
            draw_circle(flower,i,"blue")
            flower.left(90)
        for j in range (1,3):
            draw_circle(flower,i,"green")
            flower.left(90)
    flower.right(45)
    flower.color("blue")
    flower.forward(200)

    window.exitonclick()

def draw_circle(circle, radius, color):
    circle.color(color)
    circle.circle(radius)

draw_shapes()
