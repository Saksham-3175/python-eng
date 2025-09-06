def avegrage(a = 2, b = 1):
    print(f"Average is: {((a+b)/2)}")

# avegrage()

##keyword arbitrary args
def multiply(*numbers: int):
    print(type(numbers))
    product = 1
    for i in numbers:
        product *= i
    print(f"Product is: {product}")

# multiply(7)

#For dict, use **(key = value pair will be passed as dict) and for tuples, use *
def name(**input_args):
    print(f"Hello, {input_args['first_name']} {input_args['last_name']}")

# name(first_name = "Sudher", last_name = "Awasthi")

#when to use 'return'
def avegrage2(a = 3, b = 5):
    print(f"Average is: {((a+b)/2)}")

# ans2 = avegrage2()
# print(ans2) #when you print w/o using 'return' you get None at the end as the func has nothing to return.

def avegrage3(**num: int):
    print(f"First Number = {num['num1']}")
    avg = 0
    for i in num.values():
        avg += i
    average = avg/len(num.values())
    return num, float(average)
ans = avegrage3(num1=23, num2=25, num3=20)
print(ans)
