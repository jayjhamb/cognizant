# Task 1 - Working with Lists
# Create a list of favorite fruits
favorite_fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Append a new fruit to the list
favorite_fruits.append('fig')
print("After adding a fruit:", favorite_fruits)

# Remove one fruit from the list
favorite_fruits.remove('apple')
print("After removing a fruit:", favorite_fruits)

# Print the list in reverse order using slicing
print("Reversed list:", favorite_fruits[::-1])

# Task 2 - Exploring Dictionaries
# Create a dictionary with personal information
personal_info = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Add a new key-value pair for "favorite color"
personal_info["favorite color"] = "Blue"

# Update the "city" key with a new value
personal_info["city"] = "Los Angeles"

# Print all keys and values using a loop
print("Keys:", ", ".join(personal_info.keys()))
print("Values:", ", ".join(str(value) for value in personal_info.values()))

# Task 3 - Using Tuples
# Create a tuple with favorite movie, song, and book
favorite_things = ('Inception', 'Bohemian Rhapsody', '1984')

# Try to change one of the elements (this will raise an error if uncommented)
# favorite_things[0] = 'The Matrix'  # Uncomment to see the immutability error

# Print the tuple and its length
print("Favorite things:", favorite_things)
print("Length of tuple:", len(favorite_things))