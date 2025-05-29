# String Functions

# Define a sample string
sample_text = "Welcome to Python Programming!"
print(sample_text)

# 1. strip(): Remove leading and trailing spaces
stripped_text = sample_text.strip()
print("Stripped Text:", stripped_text)

# 2. lower(): Convert the string to lowercase
lower_text = stripped_text.lower()
print("Lowercase Text:", lower_text)

# 3. upper(): Convert the string to uppercase
upper_text = stripped_text.upper()
print("Upper Text:", upper_text)

# 4. title(): Convert the string to title case
title_text = stripped_text.title()
print("Title Case Text:", title_text)

# 5. replace(): Replace a substring with another
replaced_text = stripped_text.replace("Python", "Java")
print("Replaced Text:", replaced_text)

# 6. find(): Find the index of a substring
find_index = stripped_text.find("Python")
print("Index of 'Python':", find_index)

# 7. split(): Split the string into a list
split_text = stripped_text.split()
print("Split Text:", split_text)

# 8. join(): Join a list of strings into a single string
joined_text = " ".join(split_text)
print("Joined Text:", joined_text)

# 9. startswith(): Check if the string starts with a specific substring
starts_with = stripped_text.startswith("Welcome")
print("Starts with 'Welcome':", starts_with)

# 10. endswith(): Check if the string ends with a specific substring
ends_with = stripped_text.endswith("Programming!")
print("Ends with 'programming!':", ends_with)

# 11. isalpha(): Check if all characters in the string are alphabetic
alpha_check = stripped_text.replace(" ", "").isalpha()  # Ignore spaces for this check
print("Is Alphabetic:", alpha_check)

# 12. isdigit(): Check if all characters in the string are digits
digit_check = "12345".isdigit()
print("Is Digit:", digit_check)