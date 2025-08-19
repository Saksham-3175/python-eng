class Animal():
    location = "Australia"
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Bhow Bhow!"

class Dog(Animal):
    def get_breed(self):
        super().speak()
        return f"{self.location}'s breed"
    
labrador = Dog("Jack")
print(labrador.get_breed())