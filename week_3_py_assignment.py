def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
# Prompt User for input and calculate discount
try:
    original_price = float(input("Enter the original price of the item: N"))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percent)

    if discount_percent >= 20:
        discount_amount = original_price * (discount_percent / 100)
        print(f"Discount applied: {discount_percent}%")
        print(f"You saved: N{discount_amount:.2f}")
        print(f"Final price after discount: N{final_price:.2f}")
    else:
        print(f"No discount applied (discount must be 20% or higher)")
        print(f"Original price: N{original_price:.2f}")

except ValueError:
    print("Please enter a valid numeric value for price and discount percentage.")
