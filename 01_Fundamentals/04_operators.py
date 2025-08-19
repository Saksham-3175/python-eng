#Arithmetic operators: +, -, *, /, %, **
#Comparison operators: ==, !=, >, <, >=, <=
#Logical Operators(ops on bool): and, or, not
#Assignment Operators: =, +=, -=, *=, /=, %=, **=, //=
#Membership Operators: in, not in
#Identify Operatros: is, is not


def logical_operators():
    def logical_and():
        print(f"True and True: {True and True}") #T
        print(f" False and False: {False and False}") #F
        print(f" True and False: {True and False}") #F
        print(f" False and True: {False and True}") #F

    def logical_or():
        print(f"True or True: {True or True}") #T
        print(f"False or False: {False or False}") #F
        print(f"True or False: {True or False}") #T
        print(f"False or True: {False or True}") #T

    def logical_not():
        print(f"True not True: {not False}") #
        print(f"True not False: {not True}")
    return logical_and(), logical_or(), logical_not()
logical_operators()

