# Task 1 - Writing Functions
def greet_user(name):
    """Prints a personalized greeting."""
    print(f"Hello, {name}! Welcome aboard.")

def add_numbers(num1, num2):
    """Adds two numbers and returns the result."""
    return num1 + num2

# Example usage for Task 1
greet_user("Alice")
result = add_numbers(5, 10)
print(f"The sum of 5 and 10 is {result}.")

# Task 2 - Using Default Parameters
def describe_pet(pet_name, animal_type="dog"):
    """Prints a description of the pet."""
    print(f"I have a {animal_type} named {pet_name}.")

# Example usage for Task 2
describe_pet("Buddy")
describe_pet("Whiskers", "cat")

# Task 3 - Functions with Variable Arguments
def make_sandwich(*ingredients):
    """Prints the list of ingredients for a sandwich."""
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

# Example usage for Task 3
make_sandwich("Lettuce", "Tomato", "Cheese")

# Task 4 - Understanding Recursion
def factorial(n):
    """Calculates the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Calculates the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage for Task 4
fact_result = factorial(5)
fib_result = fibonacci(6)
print(f"Factorial of 5 is {fact_result}.")
print(f"The 6th Fibonacci number is {fib_result}.")