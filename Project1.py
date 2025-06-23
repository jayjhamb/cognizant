# Inventory Management Program 

# Step 1: Create the Inventory
inventory = {}

# Function to display the inventory
def display_inventory():
    if not inventory:
        print("The inventory is empty.")
    else:
        print("Current inventory:")
        for item, (quantity, price) in inventory.items():
            print(f"Item: {item}, Quantity: {quantity}, Price: ${price:.2f}")

# Function to calculate the total value of the inventory
def calculate_total_value():
    total_value = sum(quantity * price for quantity, price in inventory.values())
    print(f"Total value of inventory: ${total_value:.2f}")

# Step 2: Add, Remove, and Update Items
def add_item(item_name, quantity, price):
    if item_name in inventory:
        print(f"{item_name} already exists in the inventory. Use update_item to modify it.")
    else:
        inventory[item_name] = (quantity, price)
        print(f"{item_name} added to the inventory.")

def remove_item(item_name):
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed from the inventory.")
    else:
        print(f"{item_name} does not exist in the inventory.")

def update_item(item_name, quantity=None, price=None):
    if item_name in inventory:
        current_quantity, current_price = inventory[item_name]
        new_quantity = quantity if quantity is not None else current_quantity
        new_price = price if price is not None else current_price
        inventory[item_name] = (new_quantity, new_price)
        print(f"{item_name} updated in the inventory.")
    else:
        print(f"{item_name} does not exist in the inventory.")

# Step 3: Interactive Menu
def inventory_manager():
    print("Welcome to the Inventory Manager!")
    while True:
        print("\nOptions:")
        print("1. Display inventory")
        print("2. Add an item")
        print("3. Remove an item")
        print("4. Update an item")
        print("5. Calculate total value")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_inventory()
        elif choice == "2":
            item_name = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            price = float(input("Enter the price: "))
            add_item(item_name, quantity, price)
        elif choice == "3":
            item_name = input("Enter the item name to remove: ")
            remove_item(item_name)
        elif choice == "4":
            item_name = input("Enter the item name to update: ")
            quantity = input("Enter the new quantity (leave blank to keep current): ")
            price = input("Enter the new price (leave blank to keep current): ")
            update_item(item_name, int(quantity) if quantity else None, float(price) if price else None)
        elif choice == "5":
            calculate_total_value()
        elif choice == "6":
            print("Exiting the Inventory Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the inventory manager
inventory_manager()
