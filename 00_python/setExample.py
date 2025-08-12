# Creating a set using curly braces
fruits = {"apple", "banana", "cherry","Cherry"}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

# Creating a set using the set() constructor from a list
numbers = set([1, 2, 3, 4, 4, 2])
print(numbers)  # Output: {1, 2, 3, 4}  (duplicates removed)

# Creating an empty set (IMPORTANT: {} creates an empty dict, not a set)
empty_set = set()
print(type(empty_set))  # Output: <class 'set'>

data = [1, 2, 2, 3, 3, 4]
unique_data = set(data)
print(unique_data)  # Output: {1, 2, 3, 4}


s = {"apple", "banana"}

# Add a single element
s.add("cherry")
print(s)  # {'banana', 'cherry', 'apple'}

# Add multiple elements
s.update(["orange", "mango"])
print(s)  # {'banana', 'cherry', 'apple', 'mango', 'orange'}

# Remove element (throws error if not found)
s.remove("banana")
print(s)  # {'cherry', 'apple', 'mango', 'orange'}

# Remove element safely (no error if missing)
s.discard("grape")  # No error even if grape is not present

# Pop removes a random element
item = s.pop()
print("Removed:", item)
print("Remaining:", s)


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
print(A | B)         # {1, 2, 3, 4, 5, 6}
print(A.union(B))    # {1, 2, 3, 4, 5, 6}

# Intersection
print(A & B)         # {3, 4}
print(A.intersection(B))  # {3, 4}

# Difference (A - B: elements in A but not in B)
print(A - B)         # {1, 2}
print(A.difference(B))    # {1, 2}

# Symmetric Difference (elements in A or B, but not both)
print(A ^ B)         # {1, 2, 5, 6}
print(A.symmetric_difference(B))  # {1, 2, 5, 6}



s = {"apple", "banana", "cherry"}
print("apple" in s)     # True
print("grape" not in s) # True


# Squares of numbers from 0 to 5
squares = {x**2 for x in range(6)}
print(squares)  # {0, 1, 4, 9, 16, 25}


fs = frozenset([1, 2, 3, 4])
print(fs)  # frozenset({1, 2, 3, 4})

# fs.add(5)  # ❌ Error: 'frozenset' object has no attribute 'add'


text = "programming"
unique_chars = set(text)
print(unique_chars)  # {'r', 'p', 'm', 'a', 'o', 'n', 'i', 'g'}
