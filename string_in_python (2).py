
# Example of string methods

# Initial string
text = "   Hello World Python   "

# Convert to lowercase
print(text.lower())  # Output: "   hello world python   "

# Convert to uppercase
print(text.upper())  # Output: "   HELLO WORLD PYTHON   "

# Capitalize each word
print(text.title())  # Output: "   Hello World Python   "

# Strip leading and trailing spaces
print(text.strip())  # Output: "Hello World Python"

# Replace 'Python' with 'Programming'
print(text.replace("Python", "Programming"))  # Output: "   Hello World Programming   "

# Split the string into a list of words
print(text.split())  # Output: ['Hello', 'World', 'Python']

# Join a list of words into a single string with spaces
words = ['Hello', 'World', 'Python']
print(" ".join(words))  # Output: "Hello World Python"

# Find the position of 'World'
print(text.find("World"))  # Output: 11

# Check if the string starts with '   Hello'
print(text.startswith("   Hello"))  # Output: True

# Check if the string ends with 'Python'
print(text.endswith("Python   "))  # Output: True

# Check if the string contains only digits
print("12345".isdigit())  # Output: True

# Check if the string contains only alphabetic characters
print("Hello".isalpha())  # Output: True

### Key Points

# - **Strings are immutable:** Methods that modify a string return a new string rather than changing the original string.
# - **Method chaining:** You can chain methods together for more complex operations. For example, `text.strip().upper().replace("WORLD", "EVERYONE")`.

