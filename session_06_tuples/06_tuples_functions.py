# 06_tuples_functions
def get_student_info():
    # Returning a tuple with student information
    return ("Alice", 20, "Computer Science")

# Unpacking the tuple returned by the function
name, age, major = get_student_info()

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Major: {major}")

# The function get_student_info() returns a tuple containing a student's name, age, and major.
# The returned tuple is unpacked into name, age, and major variables.
# Finally, the values are printed.