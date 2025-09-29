import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("lightblue")   # Background color

# Create a turtle object (pen)
pen = turtle.Turtle()
pen.shape("turtle")   # Turtle shape
pen.color("green")    # Turtle color
pen.pensize(3)

# Move the turtle
pen.forward(100)    # Move forward by 100 units
pen.left(90)        # Turn left by 90 degrees
pen.forward(100)    # Move forward again
pen.right(45)       # Turn right by 45 degrees
pen.forward(70)     # Move forward by 70 units

# Keep window open until clicked
screen.exitonclick()
