try: 
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    

    print("Enter the operation you want to perform: ")
    operation = input()
    def calculate(a, b, operation):
        match operation:
            case "+":
                return f"Addition is: {(a + b)}"
            case "-":
                return f"Subtraction is: {(a - b)}"
            case "*":
                return f"{(a * b)}"
            case "/":
                return f"{(a / b)}"
            case _:
                list_of_operators = ["+", "-", "*","/"]
                if operation not in list_of_operators:
                    return f"{operation} is not a valid operator. Please select a valid operator({list_of_operators})"
    print(calculate(a, b, operation))

except Exception as e:
    print("Enter valid numbers please")

print("calculation done")

