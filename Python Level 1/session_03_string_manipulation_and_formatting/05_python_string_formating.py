# Python String Formatting
# Old Style Formatting
greet = "Hello, %s!" % "Alice" # Output: "Hello, Alice!"
print(greet)

# Using `str.format()`
greet = "hello, {}!".format("Bob") # Output: "Hello, Bob!"
print(greet)

# f-strings (Mordern and Recommended)
name = "John"
age = 30
info = f"Name: {name}, Age: {age}" # Output: "Name: John, Age: 30"
print(info)