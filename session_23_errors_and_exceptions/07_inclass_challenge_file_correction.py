# File Correction
# Function to replace a misspelled word in a file
def correct_spelling_in_file(filename, wrong_word, correct_word):
    try:
        # Step 1: Open the file and read its content
        with open(filename, 'r') as file:
            content = file.read()

        # Step 2: Replace all occurrences of the misspelled word
        updated_content = content.replace(wrong_word, correct_word)

        # Step 3: Write the corrected content back to the same file
        with open(filename, 'w') as file:
            file.write(updated_content)

        print(f"All occurrences of '{wrong_word}' have been replaced with '{correct_word}'.")
    
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print("An error occurred:", e)

# Example Usage:
filename = "programming.txt"     # The file Arunima created
wrong_word = "langauge"          # Misspelled word
correct_word = "language"        # Correct word

correct_spelling_in_file(filename, wrong_word, correct_word)
