# Local Scope
def greet():
    message = "Hello, Neil!"  # local variable
    print(message)

greet()
# print(message)  # This will raise an error
# A variable created inside a function belongs to the local scope of that function and cannot be used outside it.