import turtle

# Create a window and a turtle
window = turtle.Screen()
window.bgcolor("lightblue")
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(3)

# Draw a square
for _ in range(4):
    pen.forward(100)
    pen.right(90)

# Move to new position
pen.penup()
pen.goto(-150, 0)
pen.pendown()

# Draw a triangle
for _ in range(3):
    pen.forward(100)
    pen.left(120)

# Move to another position
pen.penup()
pen.goto(150, 0)
pen.pendown()

# Draw a circle
pen.circle(50)

# Keep window open
window.mainloop()
