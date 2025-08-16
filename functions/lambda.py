# Lambda Function Examples with Different Operations


# 2. Lambda with map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x*2, numbers))
print("\nMap Example:")
print(f"Original numbers: {numbers}")
print(f"Doubled numbers: {doubled}")

# 3. Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("\nFilter Example:")
print(f"Original numbers: {numbers}")
print(f"Even numbers: {even_numbers}")

# 4. Lambda with sort()
students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 75},
    {"name": "Charlie", "score": 93}
]

# Sort by score
sorted_by_score = sorted(students, key=lambda x: x["score"], reverse=True)
print("\nSort Example:")
print("Sorted by score (descending):")
for student in sorted_by_score:
    print(f"Name: {student['name']}, Score: {student['score']}")

# 5. Lambda with reduce()
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)
product_all = reduce(lambda x, y: x * y, numbers)
print("\nReduce Example:")
print(f"Sum of all numbers: {sum_all}")
print(f"Product of all numbers: {product_all}")

# 6. Lambda with list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [(lambda x: x**2)(x) for x in numbers]
print("\nList Comprehension with Lambda:")
print(f"Original numbers: {numbers}")
print(f"Squares: {squares}")

# 7. Multiple arguments in Lambda
rectangle_area = lambda length, width: length * width
print("\nMultiple Arguments Example:")
print(f"Area of rectangle (length=5, width=3): {rectangle_area(5, 3)}")

# 8. Lambda with conditional expression
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print("\nConditional Lambda Example:")
print(f"Is 4 even or odd? {is_even(4)}")
print(f"Is 7 even or odd? {is_even(7)}")