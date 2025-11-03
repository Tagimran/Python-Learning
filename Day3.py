# Create a list of 5 subjects → print each subject

Subjects = ["python","java","c","CSS","Html"]

for subject in Subjects:
    print (subject)

# Store 3 students’ marks in a list → find average

Marks = [56, 95, 74]
total = 0

for i in range(len(Marks)):
    total += Marks[i]

avg = total / len(Marks)
print("Average of 3 student marks:", avg)

# Create a tuple of weekdays → print only weekends

Weekends = ("monday","Tuesday","wednesday","Thusday","Friday","Saturday","Sunday")

print(f"Weakend is {Weekends[5]} and {Weekends[6]}")

# Create a dictionary for a product → print price, name

product = {
    "name": "Laptop",
    "price": 55000,
    "brand": "HP",
    "color": "Silver"
}

print("Product Name:", product["name"])
print("Product Price:", product["price"])

# Use a loop to print all keys & values

for key, value in product.items():
    print(key, ":", value)
    