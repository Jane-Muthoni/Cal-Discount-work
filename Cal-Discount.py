def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
except EOFError:
    price, discount_percent = 6900, 22

final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:
    print(f"Final price after discount: {final_price}")
else:
    print(f"No discount applied. Final price: {final_price}")
