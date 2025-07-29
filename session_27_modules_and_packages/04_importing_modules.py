# Import the whole module
import math

print(math.sqrt(16))  # Output: 4.0

# Import with an alias (renaming the module)
import math as m

print(m.pi)  # Output: 3.141592653589793

# Import specific functions or variables
from math import sqrt, pi

print(sqrt(25))  # Output: 5.0
print(pi)        # Output: 3.141592653589793

# Import all contents of a module (not recommended)
from math import *

print(sin(0))  # Output: 0.0
print(factorial(5))  # Output: 120
