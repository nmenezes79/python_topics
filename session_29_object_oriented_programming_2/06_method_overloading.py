class Greeting:
    def greet(self, name=None):
        if name is None:
            print("Hello!")
        elif isinstance(name, str):
            print(f"Hello, {name}!")
        else:
            print("Hello, stranger!")

g = Greeting()
g.greet()            # Output: Hello!
g.greet("Alice")     # Output: Hello, Alice!
g.greet(123)         # Output: Hello, stranger!
