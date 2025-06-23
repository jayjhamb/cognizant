import turtle

# Step 2: Factorial Function
def factorial(n):
    """Calculates the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Step 3: Fibonacci Function
def fibonacci(n):
    """Calculates the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Step 4: Recursive Fractal Pattern (Bonus)
def draw_fractal(branch_length, t):
    """Draws a recursive fractal tree using the turtle library."""
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_fractal(branch_length - 15, t)
        t.left(40)
        draw_fractal(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

def fractal_tree():
    """Sets up the turtle screen and draws a fractal tree."""
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.color("green")
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    draw_fractal(100, t)
    screen.mainloop()

# Step 5: User-Friendly Program
def main():
    """Main program to present a menu of recursive functions."""
    while True:
        print("\nWelcome to the Recursive Artistry Program!")
        print("Choose an option:")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci")
        print("3. Draw a Recursive Fractal")
        print("4. Exit")
        choice = input("> ")

        if choice == "1":
            try:
                num = int(input("Enter a number to find its factorial: "))
                if num < 0:
                    print("Please enter a positive integer.")
                else:
                    print(f"The factorial of {num} is {factorial(num)}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        elif choice == "2":
            try:
                num = int(input("Enter the position of the Fibonacci number: "))
                if num < 0:
                    print("Please enter a positive integer.")
                else:
                    print(f"The {num}th Fibonacci number is {fibonacci(num)}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        elif choice == "3":
            print("Drawing a fractal tree... Close the window to return to the menu.")
            fractal_tree()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()