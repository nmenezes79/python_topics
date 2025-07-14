# Aymans Files
import re

# File paths
input_file = 'ayman_file.txt'
output_file = 'ayman_modified.txt'

# Read the content of the input file
with open(input_file, 'r') as file:
    content = file.read()

# Replace each number followed by a period with a newline before it
# The regex pattern uses a lookbehind to avoid inserting newline at the beginning
modified_content = re.sub(r'(?<!^)(\d+\.)', r'\n\1', content)

# Write the modified content to a new file
with open(output_file, 'w') as file:
    file.write(modified_content)

print(f"File has been modified and saved as '{output_file}'")
