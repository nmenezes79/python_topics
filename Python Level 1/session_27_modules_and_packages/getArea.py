# getArea.py

import math

def getArea(shape, *dimensions):
    shape = shape.lower()
    
    if shape == "square":
        if len(dimensions) != 1:
            raise ValueError("Square requires 1 dimension (side).")
        side = dimensions[0]
        return side * side
    
    elif shape == "rectangle":
        if len(dimensions) != 2:
            raise ValueError("Rectangle requires 2 dimensions (length, width).")
        length, width = dimensions
        return length * width
    
    elif shape == "circle":
        if len(dimensions) != 1:
            raise ValueError("Circle requires 1 dimension (radius).")
        radius = dimensions[0]
        return math.pi * radius ** 2
    
    elif shape == "triangle":
        if len(dimensions) != 2:
            raise ValueError("Triangle requires 2 dimensions (base, height).")
        base, height = dimensions
        return 0.5 * base * height

    else:
        raise ValueError("Unsupported shape. Supported shapes: square, rectangle, circle, triangle.")
