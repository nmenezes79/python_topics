import turtle

# create turtle
pen = turtle.Turtle()

# speed values: 0 (fastest), 1 (slowest) to 10 (fast)
pen.speed(1)   # very slow
pen.forward(100)

pen.speed(5)   # medium speed
pen.forward(100)

pen.speed(10)  # very fast
pen.forward(100)

pen.speed(0)   # fastest (no animation delay)
pen.forward(100)

turtle.done()