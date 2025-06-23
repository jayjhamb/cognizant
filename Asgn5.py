# Task 1 - String Slicing and Indexing
# Create a string variable
string_var = "Python is amazing!"

# Extract and print slices
print("First word:", string_var[:6])  # First 6 characters
print("Amazing part:", string_var[10:17])  # The word "amazing"
print("Reversed string:", string_var[::-1])  # Entire string in reverse order

# Task 2 - String Methods
# Create a string with extra spaces
string_with_spaces = " hello, python world! "

# Apply string methods and print results
print("After strip():", string_with_spaces.strip())  # Remove extra spaces
print("After capitalize():", string_with_spaces.strip().capitalize())  # Capitalize first letter
print("After replace():", string_with_spaces.strip().replace("world", "universe"))  # Replace "world" with "universe"
print("After upper():", string_with_spaces.strip().upper())  # Convert to uppercase

# Task 3 - Check for Palindromes
# Ask the user to input a word
word = input("Enter a word: ")

# Check if the word is a palindrome
if word == word[::-1]:
    print(f"Yes, '{word}' is a palindrome!")
else:
    print(f"No, '{word}' is not a palindrome.")