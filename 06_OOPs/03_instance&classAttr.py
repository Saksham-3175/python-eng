class Employee:
    company = "ASUS"

    def __init__(self, company, salary) -> None:
        self.company = company
        self.salary = salary


e1 = Employee("Tesla", 23000)
#Tesla -> instance attr
#ASUS -> Class attr

#Object Introspection 
#job: finds out all the methods an object has

