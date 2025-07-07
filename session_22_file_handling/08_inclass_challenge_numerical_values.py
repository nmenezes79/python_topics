import re

def check_numerical_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            line_number = 1
            found = False
            for line in file:
                # Check if the line contains any digit using regex
                if re.search(r'\d', line):
                    print(f"Line {line_number} contains a numerical value.")
                    found = True
                line_number += 1
            
            if not found:
                print("No numerical values found in the file.")
    except FileNotFoundError:
        print("The file was not found. Please check the file name or path.")

# Example usage
check_numerical_lines("sample.txt")  # Replace 'sample.txt' with your file name
