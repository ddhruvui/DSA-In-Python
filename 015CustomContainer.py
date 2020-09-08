class TagCloud:
    def __init__(self):
        # to create private variable add __behind var
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0)+1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("Python")
cloud.add("python")

print(cloud["python"])

cloud["python"] = 10
print(cloud["python"])


#--------------------------------------------------------------------------

# python way of getting and setting property

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    # if setter is commented only once the value will be set
    # and if one tries later to change value error will be raised
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be less then or equal to zero")
        self.__price = value

# will raise error for negative argument
product = Product(1)
print(product.price)


