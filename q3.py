# Design a small Product Inventory System:

# Class Product

# Attributes: name, price, quantity

# Dunder methods:

# __str__ – readable info

# __add__ – merge two products of same name (combine quantity, average price)

# __lt__ – compare based on price

# Class Inventory

# Maintains a private list of products

# Methods:

# add_product()

# __len__() → returns total number of items

# __getitem__() → allows indexing

# search_by_name() (case-insensitive match)

# Demonstrate:

# Adding multiple products

# Sorting them using Python’s built-in sorted()

# Printing total inventory value.


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.__prods = []  # private list of products

    def add_product(self, product):
        self.__prods.append(product)

    def __len__(self):
        return len(self.__prods)

    def __getitem__(self, index):
        return self.__prods[index]

    def search_by_name(self, name):
        res = []

        for pr in self.__prods:
            if name in pr.name:
                res.append(pr)

        return res

    def total_inven_value(self):
        tot = 0

        for i in self.__prods:
            tot += i.price * i.quantity

        return tot


inven = Inventory()

inven.add_product(Product("Bread", 30, 5))
inven.add_product(Product("Eggs", 5, 10))
inven.add_product(Product("Bisi Bile Bath", 50, 2))

for pr in sorted(inven):  # sorted by price
    print(pr)

for pr in inven.search_by_name("Eggs"):  # search Eggs
    print(pr)

print("Total inventory value", inven.total_inven_value())
