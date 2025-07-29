# math_utils/                 # This is the package folder
# │
# ├── __init__.py             # Makes 'math_utils' a package
# ├── basic_ops.py            # Module for basic operations
# └── advanced_ops.py         # Module for advanced operations

# Import from package
from math_utils import add, subtract, power, factorial

print(add(5, 3))        # Output: 8
print(subtract(10, 4))  # Output: 6
print(power(2, 3))      # Output: 8
print(factorial(5))     # Output: 120
