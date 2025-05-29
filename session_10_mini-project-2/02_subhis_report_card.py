# More on Mini Project 2 - Subhi's Report Card

def calculate_grade(marks):
    return "Pass" if marks >= 50 else "Fail"

def display_report_card(marks_list):
    subjects = ["Math", "Science", "English", "History", "Computer"]
    total_marks = sum(marks_list)
    percentage = (total_marks / (len(subjects) * 100)) * 100
    
    print("=" * 40)
    print("\tS U B H I ' S  R E P O R T  C A R D")
    print("=" * 40)
    print(f"{'Subject':<15}{'Marks':<10}{'Grade':<10}")
    print("-" * 40)
    
    for subject, marks in zip(subjects, marks_list):
        grade = calculate_grade(marks)
        print(f"{subject:<15}{marks:<10}{grade:<10}")
    
    print("-" * 40)
    print(f"Total Marks: {total_marks} / {len(subjects) * 100}")
    print(f"Percentage: {percentage:.2f}%")
    print("=" * 40)

# Example marks (You can modify these values)
marks_list = [75, 45, 88, 62, 49]
display_report_card(marks_list)
