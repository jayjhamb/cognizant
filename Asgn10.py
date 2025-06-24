# Task 1 - Understanding Python Exceptions
def divide_by_number():
    while True:
        try:
            number = int(input("Enter a number: "))
            result = 100 / number
            print(f"100 divided by {number} is {result}.")
            break
        except ZeroDivisionError:
            print("Oops! You cannot divide by zero.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Task 2 - Types of Exceptions
def handle_exceptions():
    # IndexError: Accessing an invalid list index
    try:
        my_list = [1, 2, 3]
        print(my_list[5])  # Invalid index
    except IndexError:
        print("IndexError occurred! List index out of range.")

    # KeyError: Accessing a non-existent key in a dictionary
    try:
        my_dict = {"name": "Alice"}
        print(my_dict["age"])  # Key does not exist
    except KeyError:
        print("KeyError occurred! Key not found in the dictionary.")

    # TypeError: Adding a string and an integer
    try:
        result = "hello" + 5  # Invalid operation
    except TypeError:
        print("TypeError occurred! Unsupported operand types.")

# Task 3 - Using try...except...else...finally
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    else:
        print(f"The result is {result}.")
    finally:
        print("This block always executes.")

# Main program to run all tasks
if __name__ == "__main__":
    print("Task 1: Understanding Python Exceptions")
    divide_by_number()

    print("\nTask 2: Types of Exceptions")
    handle_exceptions()

    print("\nTask 3: Using try...except...else...finally")
    divide_numbers()