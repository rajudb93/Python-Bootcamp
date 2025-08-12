# Customer Profile Management - Dictionary Demo

# 1) Create the dictionary
customer = {
    "name": "John Doe",
    "age": 32,
    "city": "New York"
}

# 2) Print the dictionary
print("Initial customer dict:", customer)

# 3) Add "email" and "phone"
customer["email"] = "john.doe@example.com"
customer["phone"] = "+1-555-0100"

# 4) Print the updated dictionary
print("\nAfter adding email & phone:", customer)

# 5) Print customer's "name" and "city"
print("\nCustomer name:", customer["name"])
print("Customer city:", customer["city"])

# 6) Check whether the key "email" exists
has_email = "email" in customer
print("\nDoes 'email' exist?:", has_email)

# 7) Delete the "age" field
del customer["age"]

# 8) Print the updated dictionary
print("\nAfter deleting 'age':", customer)

# 9) Print keys, values, and items
print("\nAll keys:", list(customer.keys()))
print("All values:", list(customer.values()))
print("All items:", list(customer.items()))

# 10) Remove and print the last inserted key-value pair
last_inserted = customer.popitem()  # removes the last inserted item
print("\nRemoved last inserted item:", last_inserted)
print("Dictionary after popitem():", customer)

# 11) Use .get() to access a non-existent key "membership"
membership_status = customer.get("membership")  # returns None if not found
print("\nMembership status (via get):", membership_status)

# 12) Update with a new field "address"
customer.update({"address": "221B Baker Street"})

# 13) Print the final dictionary
print("\nFinal customer dict:", customer)
