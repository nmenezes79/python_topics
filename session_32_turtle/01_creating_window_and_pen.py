import turtle

# Create a window
window = turtle.Screen()
window.title("My First Window")
window.bgcolor("lightblue")

# Create a pen (turtle)
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("darkblue")
pen.pensize(3)

# Draw a square using the pen
for _ in range(4):
    pen.forward(100)   # Move forward 100 units
    pen.right(90)      # Turn right 90 degrees

# Keep the window open until clicked
window.exitonclick()
