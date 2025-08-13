customer_name = "Amit"
customer_age = 24
total_purchase = 1200

if total_purchase > 1000:
    print(f"eligible for discount")
else:
    print(f"not eligible for discount")
    
if customer_age >= 60:  
    print("Customer is senior citizen, eligible for additional discount")