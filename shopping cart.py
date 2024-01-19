# Product Catalog - Product Name: Product Price
product_prices = {'A': 20, 'B': 40, 'C': 50}

# User Inputs
quantities = {}
gift_wrappers = {}

for product in product_prices:
    quantities[product] = int(input(f"How many units of \"Item {product}\" would you like to order? \n"))
    gift_wrappers[product] = int(input(f"How many \"Item {product}\" with Gift Wrapping would you like? \n"))

# Bill
separator_line = "_____________"

# Display Table
print("Item - Quantity - Total Amount")
print(separator_line)

total_amount = 0
for product, price in product_prices.items():
    quantity = quantities[product]
    total_product_amount = quantity * price
    print(f"Item {product} - {quantity} - ${total_product_amount}")
    total_amount += total_product_amount

# SubTotal
print(separator_line)
print("Total : $", total_amount)

# Discounts
discounts = {}

if total_amount > 200:
    discounts["10% off"] = 10

for product in product_prices:
    if quantities[product] > 10:
        discounts["5% Bulk Discount"] = sum(0.05 * (quantities[prod] * product_prices[prod]) for prod in product_prices)

if sum(quantities.values()) > 20:
    discounts["10% Bulk Discount"] = 0.1 * total_amount

if sum(quantities.values()) > 30:
    tiered_discount = sum(0.5 * ((quantities[prod] - 15) * product_prices[prod]) for prod in product_prices if
                          quantities[prod] > 15)
    discounts["50% Tiered Discount"] = tiered_discount

# Apply Beneficial Discount
max_discount = max(discounts.values())
discount_name = [key for key, value in discounts.items() if value == max_discount][0]

print(separator_line)
print("Discount Applied :", discount_name)
print("Discount Amount : $", max_discount)

# Shipping Fee
shipping_items = sum(quantities.values())
shipping_fee = int((shipping_items / 10) * 5)
print('Shipping Fee : $', shipping_fee)

# Gift Wrapper Fee
gift_wrapper_fee = sum(gift_wrappers.values())
print('Gift Wrapper Fee: $', gift_wrapper_fee)

# Calculate Total
total_cost = total_amount - max_discount + shipping_fee + gift_wrapper_fee
print(separator_line)
print("Total : $", total_cost)
print(separator_line)