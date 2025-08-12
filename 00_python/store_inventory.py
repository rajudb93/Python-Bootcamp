# Managing Store Inventory

# Creating sets for Branch A and Branch B products
branch_a_products = {"bread", "milk", "butter", "jam"}
branch_b_products = {"bread", "cheese", "butter", "ketchup"}

# Print both sets
print("Branch A Products:", branch_a_products)
print("Branch B Products:", branch_b_products)

# Union of both branches’ products
all_products = branch_a_products | branch_b_products
print("\nUnion of both branches' products:", all_products)

# Intersection of both branches’ products
common_products = branch_a_products & branch_b_products
print("Common products:", common_products)

# Products in branch_a but not in branch_b
unique_to_a = branch_a_products - branch_b_products
print("Products only in Branch A:", unique_to_a)

# Check whether "ketchup" is in Branch A
is_ketchup_in_a = "ketchup" in branch_a_products
print("Is ketchup in Branch A?", is_ketchup_in_a)

# Frozenset for essential items
essential_items = frozenset(["milk", "bread", "ketchup"])
print("\nEssential Items (frozen set):", essential_items)
