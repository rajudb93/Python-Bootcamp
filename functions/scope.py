# Demonstrating Global and Nonlocal Scope in Python

# Global variable
counter = 0

def outer_function():
    # Variable in outer function's scope
    message = "Hello"
    
    def inner_function():
        # Using nonlocal to modify outer function's variable
        nonlocal message
        message = "Hi"
        
        # Using global to modify global variable
        global counter
        counter += 1
        
        print(f"Inner function - message: {message}")
        print(f"Inner function - counter: {counter}")
    
    print(f"Before inner call - message: {message}")
    print(f"Before inner call - counter: {counter}")
    
    inner_function()
    
    print(f"After inner call - message: {message}")
    print(f"After inner call - counter: {counter}")

# Test the scope
print(f"Before outer call - counter: {counter}")
outer_function()
print(f"After outer call - counter: {counter}")