import logging

# Step 4: Configure logging to log errors to a file
logging.basicConfig(filename="error_log.txt", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

def get_number(prompt):
    """Prompt the user for a number and validate the input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def addition():
    """Perform addition."""
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    return num1 + num2

def subtraction():
    """Perform subtraction."""
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    return num1 - num2

def multiplication():
    """Perform multiplication."""
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    return num1 * num2

def division():
    """Perform division with exception handling."""
    num1 = get_number("Enter the first number: ")
    while True:
        try:
            num2 = get_number("Enter the second number: ")
            result = num1 / num2
            return result
        except ZeroDivisionError as e:
            print("Oops! Division by zero is not allowed.")
            logging.error(f"ZeroDivisionError occurred: {e}")

def main():
    """Main program to display the menu and handle user input."""
    print("Welcome to the Error-Free Calculator!")
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("> ")

        try:
            if choice == "1":
                print(f"The result is: {addition()}")
            elif choice == "2":
                print(f"The result is: {subtraction()}")
            elif choice == "3":
                print(f"The result is: {multiplication()}")
            elif choice == "4":
                print(f"The result is: {division()}")
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please select a valid option.")
        except Exception as e:
            print("An unexpected error occurred. Please try again.")
            logging.error(f"Unexpected error: {e}")
        finally:
            print("Thank you for using the calculator!")

# Run the program
if __name__ == "__main__":
    main()