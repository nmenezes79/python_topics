# Creating a dictionary to store Chris's marks
chris_marks = {
    "Math": 85,
    "Science": 90,
    "English": 88,
    "History": 76,
    "Computer Science": 95
}

# Creating a nested dictionary to store the marks of the entire class
class_marks = {
    "Chris": {
        "Math": 85,
        "Science": 90,
        "English": 88,
        "History": 76,
        "Computer Science": 95
    },
    "Emma": {
        "Math": 78,
        "Science": 85,
        "English": 82,
        "History": 80,
        "Computer Science": 89
    },
    "Liam": {
        "Math": 92,
        "Science": 88,
        "English": 91,
        "History": 79,
        "Computer Science": 94
    }
}

# Printing Chris's marks
print("Chris's Marks:")
for subject, marks in chris_marks.items():
    print(f"{subject}: {marks}")

# Printing the entire class marks
print("\nClass Marks:")
for student, subjects in class_marks.items():
    print(f"\n{student}:")
    for subject, marks in subjects.items():
        print(f"  {subject}: {marks}")
