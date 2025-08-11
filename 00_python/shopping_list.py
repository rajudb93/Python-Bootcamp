# Shopping List Operations for Grocery App

# 1. Create a grocery list
my_cart = ["apples", "bananas", "milk"]
print("Initial grocery list:", my_cart)

# 2. Add "bread" to the end
my_cart.append("bread")
print("After adding bread:", my_cart)

# 3. Insert "ketchup" at the beginning
my_cart.insert(0, "ketchup")
print("After inserting ketchup at the beginning:", my_cart)

# 4. Remove "bananas"
my_cart.remove("bananas")
print("After removing bananas:", my_cart)

# 5. Remove the last item and store it
removed_item = my_cart.pop()
print("Removed item:", removed_item)

# 6. Extend with "rice" and "butter"
my_cart.extend(["rice", "butter"])
print("After extending with rice and butter:", my_cart)

# 7. Sort alphabetically
my_cart.sort()
print("Sorted grocery list:", my_cart)

# 8. Reverse the list
my_cart.reverse()
print("Reversed grocery list:", my_cart)

# 9. Concatenate with another list
other_items = ["juice", "jam"]
combined_list = my_cart + other_items
print("After concatenation:", combined_list)

# 10. Duplicate the grocery list twice
duplicated_list = my_cart * 2
print("Duplicated grocery list:", duplicated_list)

# 11. Convert string to list
veggies = "tomato cucumber spinach"
veggie_list = veggies.split()
print("Converted veggie list:", veggie_list)
