# Mini Project 2 - Exam Preparation

# Taking input for 5 subjects
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i} (out of 100): "))
    marks.append(mark)

# Calculate total marks and percentage
total_marks = sum(marks)
full_marks = 500  # 5 subjects, each out of 100
percentage = (total_marks / full_marks) * 100

# Display the results
print("\nTotal Marks Obtained:", total_marks)
print("Total Full Marks:", full_marks)
print(f"Percentage Scored: {percentage:.2f}%")

# 75, 45, 88, 62, 49