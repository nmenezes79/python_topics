# String Literals

# Escape sequences in strings
escaped_string = "He said, \"Python is awesome!\""
print(escaped_string)

# Raw strings (ignoring escape sequences)
raw_string = r"C:\Users\Name\documents"
print(raw_string)

# Unicode string
unicode_string = u"Hello, \u2764!" # Unicode for a heart symbol
print(unicode_string)

# Byte string
byte_string = b"This is a byte string."
print(byte_string)

# f-strings (formatted string literals)
name = "John"
f_string = f"Hello, {name}!"
print(f_string)