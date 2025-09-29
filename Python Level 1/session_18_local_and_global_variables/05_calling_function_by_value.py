# Calling a Function By Value
def modify_value(x):
    x = x + 10
    print("Inside function, x =", x)

a = 5
modify_value(a)
print("Outside function, a =", a)