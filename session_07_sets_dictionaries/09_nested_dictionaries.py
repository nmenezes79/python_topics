# A nested dictionary in Python is a dictionary within another dictionary. 
# It allows you to store structured data in a hierarchical way,
# making it useful for representing complex relationships.

# Creating a Nested Dictionary
# A nested dictionary can be created by defining a dictionary inside another dictionary:
student_data = {
    "John": {
        "age": 20,
        "major": "Computer Science",
        "grades": {"math": 90, "science": 85}
    },
    "Alice": {
        "age": 22,
        "major": "Biology",
        "grades": {"math": 80, "science": 95}
    }
}

