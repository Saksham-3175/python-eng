#Try, Except, Finally
#Example


a = input("Enter a number to print it's multiplication table: ")

def table(a):
    for i in range(1,6):
        print(f"{int(a)} x {i} = {i * int(a)}")

    
try:
    table(a)
except:
    print(f"Nah...! I neeed a number, you entered '{a}'")

print("These are the important lines of code....")