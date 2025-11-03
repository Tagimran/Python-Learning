# 🧾 Simple Billing System
# -------------------------
# Requirements:
#   → Take item name, quantity, and price
#   → Calculate total = price × quantity
#   → Add 18% GST
#   → Print final bill clearly

print("Simple Billing System")
print("-" * 30)

# Step 1: Take user inputs
item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item (₹): "))

# Step 2: Calculate total (without GST)
total = price * quantity

# Step 3: Calculate GST (18%)
gst = total * 0.18

# Step 4: Calculate final amount
final_amount = total + gst

# Step 5: Display final bill
print("\n" + "=" * 30)
print("FINAL BILL")
print("=" * 30)
print(f"Item Name   : {item_name}")
print(f"Quantity    : {quantity}")
print(f"Price/Item  : ₹{price:.2f}")
print("-" * 30)
print(f"Total       : ₹{total:.2f}")
print(f"GST (18%)   : ₹{gst:.2f}")
print("=" * 30)
print(f"Grand Total : ₹{final_amount:.2f}")
print("=" * 30)
print("Thank you for shopping with us!")

