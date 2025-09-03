class Laptop:
    Brand = "Asus"
    Model = "TUF"
    Series = 15
    Category = "Gaming"

    def get_price(self):
        return "78000/-"

specs = Laptop() #object

print(specs.get_price())