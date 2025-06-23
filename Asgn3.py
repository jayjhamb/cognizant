# Task 1: Countdown Timer
# Ask the user for a starting number
start_number = int(input("Enter the starting number: "))

# Use a while loop to count down to 1
while start_number > 0:
    print(start_number, end=" ")
    start_number -= 1

# Print the celebratory message
print("Blast off! We have reached zero!")

# Task 2: Multiplication Table
# Ask the user to input a number
number = int(input("Enter a number: "))

# Use a for loop to generate the multiplication table
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Task 3: Find the Factorial
# Ask the user for a number
num = int(input("Enter a number: "))

# Initialize the factorial result
factorial = 1

# Use a for loop to calculate the factorial
for i in range(1, num + 1):
    factorial *= i

# Print the result
print(f"The factorial of {num} is {factorial}.")