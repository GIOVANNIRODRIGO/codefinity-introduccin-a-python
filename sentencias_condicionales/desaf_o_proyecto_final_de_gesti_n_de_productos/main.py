# Input variables
days_until_expiration = 7  # Example value
stock_level = 40  # Example value
product_type = "Non Perishable"  # Can be "Perishable" or "Non-Perishable"
if product_type == "Perishable":
    if stock_level > 50:
        if days_until_expiration <= 3:
            print("30% discount applied")
        elif days_until_expiration < 7:
            print("20% discount applied")
    else:
        if days_until_expiration >= 7:
            print("10% discount applied")
else:
    print("No discount available for non-perishable items.")