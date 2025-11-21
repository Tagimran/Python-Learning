from bill import calculate_total

cart = {}

while True:
    item = input("Enter item name: ")
    qty = int(input("Enter quantity: "))
    cart[item] = qty

    more = input("Add more? (y/n): ")
    if more.lower() != 'y':
        break

print("\nBILL TOTAL =", calculate_total(cart))
