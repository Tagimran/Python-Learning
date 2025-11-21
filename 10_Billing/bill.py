from items import items

def calculate_total(cart):
    total = 0
    for item, qty in cart.items():
        price = items.get(item, 0)
        total += price * qty
    return total
