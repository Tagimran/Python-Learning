# Class Book with title, author → save books to file

class Book :
    def __init__(self,title ,author):
        self.title= title
        self.author=author

    # Save book to file
    def save(self):
        with open("Book.txt", "a") as f:
            f.write(f"{self.title},{self.author}\n")

    # Load and display all books
    @staticmethod
    def load_all():
        Books = []
        with open("Book.txt","r") as f:
            for line in f:
                title, author = line.strip().split(",")
                Books.append(Book(title,author))
        return Books
    
# Class Product with name & price → save & retrieve products

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    #save product
    def save(self):
        with open("product.txt","a") as f:
            f.write(f"{self.name},{self.price}\n")

    #fetch all products return objects list 
    @staticmethod
    def get_all():
        products =[]
        with open("product.txt","r") as f:
            for line in f:
                name, price = line.strip().split(",")
                products.append(Product(name, price))
        return products

# Read file and create object list

# Search a record by name

def search_in_file(filename, search_name):
    with open (filename, "r") as f:
        for line in f:
            name = line.split(",")[0]
            if name.lower() == search_name.lower():
                return "FOUND: "+ line.strip()
    return "NOT FOUND"

# Delete a record from file (rewrite file without that line)

def delete_record(filename, delete_name):
    lines=[]

    #read all lines
    with open(filename,"r") as f:
        for line in f:
            name = line.split(",")[0]
            if name.lower() != delete_name.lower():
                lines.append(line)

    #rewrite file without deleted record
    with open(filename,"w") as f:
        for line in lines:
            f.write(line)
    
    return "deleted (if exited)."

# Demo / Testing

if __name__ == "__main__":

    # Add books
    b1 = Book("Python Basics", "Imran")
    b1.save()

    b2 = Book("OOP Mastery", "Rehan")
    b2.save()

    # Add products
    p1 = Product("Laptop", 55000)
    p1.save()

    p2 = Product("Mouse", 499)
    p2.save()

    # Display all books
    print("\nAll Books:")
    for b in Book.load_all():
        print(b.title, "-", b.author)

    # Display all products
    print("\nAll Products:")
    for p in Product.get_all():
        print(p.name, "-", p.price)

    # Search record
    print("\nSearch Book:", search_in_file("Book.txt", "Python Basics"))
    print("Search Product:", search_in_file("product.txt", "Mouse"))

    # Delete record
    print("\n", delete_record("product.txt", "Mouse"))