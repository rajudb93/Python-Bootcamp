# Accept multiple values from user, add them, and print the sum

numbers = input("Enter numbers separated by spaces: ")
num_list = [float(num) for num in numbers.split()]
total = sum(num_list)
print(f"The sum is: {total}")