import turtle

# create a turtle object
pen = turtle.Turtle()

# set pen size
pen.pensize(5)   # thickness of the line will be 5
# alternatively: pen.width(5)

# draw a square with thick lines
for _ in range(4):
    pen.forward(100)
    pen.right(90)

turtle.done()
