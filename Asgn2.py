# Voter Eligibility Checker 

# Step 1: Ask the user's age
age = int(input("How old are you? "))

# Step 2: Decide the eligibility
if age >= 18:
    # User is eligible to vote
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    # User is not eligible yet, calculate years to wait
    years_to_wait = 18 - age
    print(f"Oops! You’re not eligible yet. But hey, only {years_to_wait} more year(s) to go!")

