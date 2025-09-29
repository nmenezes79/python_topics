# Command
# | Command               | Description                              |
# --------------------- | ---------------------------------------- |
# `import turtle`       | Import the turtle library.               |
# `t = turtle.Turtle()` | Create a turtle object.                  |
# `t.forward(100)`      | Move turtle forward by 100 pixels.       |
# `t.backward(50)`      | Move turtle backward by 50 pixels.       |
# `t.right(90)`         | Turn turtle right by 90 degrees.         |
# `t.left(90)`          | Turn turtle left by 90 degrees.          |
# `t.penup()`           | Lift the pen so it doesn’t draw.         |
# `t.pendown()`         | Put the pen down to draw.                |
# `t.pensize(3)`        | Change the thickness of the pen.         |
# `t.pencolor("red")`   | Change the pen color.                    |
# `t.speed(1)`          | Set speed (1 slow – 10 fast).            |
# `turtle.done()`       | Finish drawing and keep the window open. |

import turtle

# Step 1: Create turtle
t = turtle.Turtle()
t.speed(3)          # Set drawing speed
t.pensize(2)        # Set pen thickness
t.pencolor("blue")  # Set pen color

# Step 2: Draw a star
for i in range(5):
    t.forward(100)  # Move forward by 100 pixels
    t.right(144)    # Turn right by 144 degrees

# Step 3: Finish
turtle.done()
