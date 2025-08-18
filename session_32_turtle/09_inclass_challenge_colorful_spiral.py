import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Magical Colorful Spiral")
turtle.colormode(255)

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Generate rainbow colors
num_colors = 100
colors = [colorsys.hsv_to_rgb(i/num_colors, 1, 1) for i in range(num_colors)]
colors = [(int(r*255), int(g*255), int(b*255)) for r, g, b in colors]

# Spiral parameters
angle = 59
distance = 1
color_index = 0

# Draw endless spiral
while True:
    pen.pencolor(colors[color_index % num_colors])
    pen.forward(distance)
    pen.right(angle)
    
    # Gradually increase distance for spiral effect
    distance += 0.5
    color_index += 1
