# Create a List, Tuple, and Dictionary
my_list = [10, 20, 30, 40, 50]  # List
my_tuple = ('a', 'b', 'c', 'd', 'e')  # Tuple
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'USA', 'hobby': 'reading'}  # Dictionary

# Access elements from the List
print("First element in the list:", my_list[0])  # Access the first element
print("Last element in the list:", my_list[-1])  # Access the last element
print("Slice of list (2nd to 4th elements):", my_list[1:4])  # Access a slice

# Access elements from the Tuple
print("Second element in the tuple:", my_tuple[1])  # Access the second element
print("Slice of tuple (3rd to 5th elements):", my_tuple[2:5])  # Access a slice

# Access elements from the Dictionary
print("Value of 'name' key:", my_dict['name'])  # Access value by key
print("Value of 'hobby' key:", my_dict['hobby'])  # Access value by key

# Additional Examples:
# Modify an element in the list
my_list[2] = 99  # Change the third element in the list
print("Modified list:", my_list)

# Try to modify the tuple (immutable)
try:
    my_tuple[2] = 'z'
except TypeError as e:
    print("Error when trying to modify a tuple:", e)

# Add a new key-value pair to the dictionary
my_dict['profession'] = 'Engineer'
print("Updated dictionary:", my_dict)
