# Simple Python Starter Script

def greet(name):
    print("Hello, " + name + "!")
def add_numbers(a, b):
    return a + b

# Main function to demonstrate basic Python features
def main():
    # Input from user
    name = input("Enter your name: ")
    greet(name)Hari

    # Variables and arithmetic
    x = 5
    y = 10
    print(str(x) + " + " + str(y) + " = " + str(add_numbers(x, y)))

    # Conditional
    if x < y:
        print(str(x) + " is less than " + str(y))
    else:
        print(str(x) + " is not less than " + str(y))

    # Loop
    print("Counting from 1 to 5:")
    for i in range(1, 6):
        print(i)

    # List
    fruits = ["apple", "banana", "cherry"]
    print("Fruits list:")
    for fruit in fruits:
        print(fruit)

if __name__ == "__main__":
    main()