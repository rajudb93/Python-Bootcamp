# Important operations that can be performed with a Python list

# List creation
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print("First fruit:", fruits[0])

# Modifying elements
fruits[1] = "orange"
print("After modification:", fruits)

# Adding elements
fruits.append("grape")           # Add at end
fruits.insert(1, "mango")        # Insert at index 1
print("After adding elements:", fruits)

# Removing elements
fruits.remove("apple")           # Remove by value
removed = fruits.pop()           # Remove last element
print("Removed:", removed)
print("After removing elements:", fruits)

# List length
print("Number of fruits:", len(fruits))

# Iterating through list
print("All fruits:")
for fruit in fruits:
    print(fruit)

# Slicing a list
print("First two fruits:", fruits[:2])

# List concatenation
more_fruits = ["kiwi", "melon"]
all_fruits = fruits + more_fruits
print("All fruits after concatenation:", all_fruits)

# Membership test
if "mango" in fruits:
    print("Mango is in the list.")

# Sorting a list
fruits.sort()
print("Sorted fruits:", fruits)

# Reversing a list
fruits.reverse()
print("Reversed fruits:", fruits)

# Copying a list
fruits_copy = fruits.copy()
print("Copy of fruits:", fruits_copy)

# Clearing a list
fruits.clear()
print("After clearing:", fruits)