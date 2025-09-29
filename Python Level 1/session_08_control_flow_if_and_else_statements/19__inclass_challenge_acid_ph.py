def determine_solution_nature(ph_level):
    if 1 <= ph_level <= 3:
        return "Strong Acid"
    elif 4 <= ph_level <= 6:
        return "Weak Acid"
    elif ph_level == 7:
        return "Neutral"
    elif 8 <= ph_level <= 11:
        return "Weak Base"
    elif 12 <= ph_level <= 14:
        return "Strong Base"
    else:
        return "Not a valid pH level"

# Taking user input
try:
    ph_level = float(input("Enter the pH level: "))
    print("The solution is:", determine_solution_nature(ph_level))
except ValueError:
    print("Please enter a valid number.")
