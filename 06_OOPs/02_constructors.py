# __init__ runs automatically everytime an object is created
#Job: setup the object with all the starting data it needs
#W/o it: Mnaually set the data you need after creating a object.


#Before constructor:
# class Laptop:
#     pass

# creating laptops
# l1 = Laptop()
# l1.brand = "Dell"
# l1.ram = 16
# l1.storage = 512

# l2 = Laptop()
# l2.brand = "Apple"
# l2.ram = 8
# l2.storage = 256

# print(l1.brand, l1.ram, l1.storage)
# print(l2.brand, l2.ram, l2.storage)

#After/ With __init__

class Laptop():
    def __init__(self, brand, series, category, price):
        self.brand = brand
        self.series = series
        self.category = category
        self.price = price

    def get_info(self):
        return f"{self.brand}'s {self.series}({self.category}) costs {self.price}/-"
    
    def is_usecase_ready(self):
        # return self.ram >= 16 and self.storage >= 512
        match self.category:
            case "Gaming":
                return f"Yes! {self.brand}'s laptops are {self.category} ready"
            case "General":
                return f"Yes! {self.brand}'s laptops are {self.category} ready"
            case _:
                return "Invalid"

l1 = Laptop("Dell", "Inspiron", "General", 35000)
l2 = Laptop("Asus", "TUF", "Gaming", 78000)
l3 = Laptop("Asus", "ProArt", "Creative", 120000)

# print(l2.get_info())

# print(l1.is_usecase_ready())

print(dir(l1))
#the __dunder__ that I didn't define: Python defined them so that each new object works correctly and does not fuck up the interpreter

