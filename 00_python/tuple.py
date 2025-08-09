

# Tuple creation
masala = ("paper", "turmeric", "chili powder", "cumin", "coriander",
          "garam masala", "cinnamon", "cardamom", "cloves", "bay leaf")

# Accessing elements
print("First spice:", masala[0])
print("Last spice:", masala[-1])

# Tuple length
print("Total spices:", len(masala))

# Iterating through tuple
print("All spices:")
for spice in masala:
    print(spice)

# Slicing a tuple (first 3 spices)
print("First three spices:", masala[:3])

# Membership test
if "ginger" in masala:
    print("Ginger is in the masala tuple.")
else:
    print("Ginger is NOT in the masala tuple.")

# Tuple concatenation
extra = ("ginger", "mustard")
all_spices = masala + extra
print("All spices after adding more:", all_spices)

# Tuple repetition
repeat = ("salt",) * 3
print("Tuple with repeated salt:", repeat)

# Unpacking tuple
first, second, *rest = masala
print("First spice:", first)
print("Second spice:", second)
print("Rest of the spices:", rest)


