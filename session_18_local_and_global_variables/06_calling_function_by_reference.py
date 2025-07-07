# Calling a Function By Reference
def modify_list(my_list):
    my_list.append(100)
    print("Inside function:", my_list)

# Original list
numbers = [1, 2, 3]
modify_list(numbers)

print("Outside function:", numbers)