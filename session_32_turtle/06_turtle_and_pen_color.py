import turtle

# Create a window
window = turtle.Screen()
window.bgcolor("lightblue")   # background color

# Create a turtle
pen = turtle.Turtle()
pen.pensize(3)   # pen size
pen.speed(5)     # drawing speed

# Set pen color and fill color
pen.color("red", "yellow")   # pen color = red, fill color = yellow

# Start filling the shape
pen.begin_fill()

# Draw a square
for _ in range(4):
    pen.forward(100)
    pen.left(90)

# End filling
pen.end_fill()

# Keep window open until click
window.exitonclick()
