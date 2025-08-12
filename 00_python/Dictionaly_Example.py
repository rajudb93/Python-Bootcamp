# Using curly braces
student = {"name": "Alice", "age": 20, "grade": "A"}
print(student)  # {'name': 'Alice', 'age': 20, 'grade': 'A'}

# Using dict() constructor
employee = dict(name="Bob", position="Manager", salary=50000)
print(employee)  # {'name': 'Bob', 'position': 'Manager', 'salary': 50000}

# Empty dictionary
empty_dict = {}
print(type(empty_dict))  # <class 'dict'>


student = {"name": "Alice", "age": 20}

# Using key directly
print(student["name"])  # Alice

# Using get() (avoids error if key not found)
print(student.get("grade", "Not Available"))  # Not Available


student = {"name": "Alice", "age": 20}

# Add new key-value
student["grade"] = "A"
print(student)  # {'name': 'Alice', 'age': 20, 'grade': 'A'}

# Update existing value
student["age"] = 21
print(student)  # {'name': 'Alice', 'age': 21, 'grade': 'A'}

# Update multiple keys
student.update({"age": 22, "grade": "B"})
print(student)  # {'name': 'Alice', 'age': 22, 'grade': 'B'}


student = {"name": "Alice", "age": 20, "grade": "A"}

# Remove and return value
age = student.pop("age")
print(age)       # 20
print(student)   # {'name': 'Alice', 'grade': 'A'}

# Remove last inserted item (Python 3.7+ maintains insertion order)
last_item = student.popitem()
print(last_item)  # ('grade', 'A')
print(student)    # {'name': 'Alice'}

# Delete a key
del student["name"]
print(student)    # {}


student = {"name": "Alice", "age": 20, "grade": "A"}

# Loop through keys
for key in student:
    print(key, student[key])

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")


# Create a dictionary of squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


students = {
    "S1": {"name": "Alice", "age": 20},
    "S2": {"name": "Bob", "age": 22}
}
print(students["S1"]["name"])  # Alice


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = dict1 | dict2
print(merged)  # {'a': 1, 'b': 3, 'c': 4}
