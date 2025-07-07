import os

# Create a sample file to delete
with open("sample.txt", "w") as file:
    file.write("This is a test file.")

# Check if the file exists, then delete it
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print("File deleted successfully.")
else:
    print("The file does not exist.")
