import turtle

# Create a screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create a turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("green")

# Default turtle size
pen.stamp()

# Increase size (stretch turtle width, length, outline thickness)
pen.turtlesize(stretch_wid=3, stretch_len=3, outline=2)
pen.color("red")
pen.stamp()

# Smaller turtle
pen.turtlesize(stretch_wid=1, stretch_len=2, outline=1)
pen.color("blue")
pen.stamp()

# Keep window open
screen.mainloop()
