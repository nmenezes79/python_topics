# Enclosed Scope
def outer_function():
    message = "Hello from Outer Function"

    def inner_function():
        print(message)  # Accessing 'message' from the outer_function

    inner_function()

outer_function()