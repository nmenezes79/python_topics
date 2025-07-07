import os

# Rename file from old_name.txt to new_name.txt
old_name = "example.txt"
new_name = "new_example.txt"

try:
    os.rename(old_name, new_name)
    print(f"File renamed from '{old_name}' to '{new_name}' successfully.")
except FileNotFoundError:
    print(f"The file '{old_name}' does not exist.")
except PermissionError:
    print("You don't have permission to rename this file.")
except Exception as e:
    print(f"An error occurred: {e}")
