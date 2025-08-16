# Basic Calculator Functions with Return Values

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    return "Cannot divide by zero"

# Test the calculator functions
num1 = 10
num2 = 5

print(f"Numbers: {num1} and {num2}")
print(f"Addition: {add(num1, num2)}")
print(f"Subtraction: {subtract(num1, num2)}")
print(f"Multiplication: {multiply(num1, num2)}")
print(f"Division: {divide(num1, num2)}")

# Test division by zero
print(f"Division by zero: {divide(num1, 0)}")