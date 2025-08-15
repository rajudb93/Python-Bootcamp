
# Food Menu Selector using match-case (Python 3.10+)
item = input("Enter food item: ").lower()

match item:
    case "pizza":
        print("Price: 30 bucks")
        
    case "burger":
        print("Price: 15 bucks")
    case "pasta":
        print("Price: 20 bucks")
    case "salad":
        print("Price: 10 bucks")
    case _:
        print("Item not available")
