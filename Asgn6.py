import string

# Step 1: Input the Password
password = input("Enter a password: ")

# Step 2: Evaluate the Password
# Initialize variables for checks
length_check = len(password) >= 8
uppercase_check = any(char.isupper() for char in password)
lowercase_check = any(char.islower() for char in password)
digit_check = any(char.isdigit() for char in password)
special_char_check = any(char in string.punctuation for char in password)

# Collect feedback for failed checks
feedback = []
if not length_check:
    feedback.append("at least 8 characters")
if not uppercase_check:
    feedback.append("at least one uppercase letter")
if not lowercase_check:
    feedback.append("at least one lowercase letter")
if not digit_check:
    feedback.append("at least one digit")
if not special_char_check:
    feedback.append("at least one special character")

# Print results
if all([length_check, uppercase_check, lowercase_check, digit_check, special_char_check]):
    print("Your password is strong!")
else:
    print(f"Your password needs {', '.join(feedback)}.")

# Bonus Challenge: Password Strength Meter
strength_score = 0
if length_check:
    strength_score += 2
if uppercase_check:
    strength_score += 2
if lowercase_check:
    strength_score += 2
if digit_check:
    strength_score += 2
if special_char_check:
    strength_score += 2

print(f"Password Strength Meter: {strength_score}/10")