#Lambda functions

square = lambda x: x * x
# print(square(5))

avg = lambda x, y, z: (x + y + z)/3
print(f"Average: {avg(3, 52, 56)}")

numbers = [1, 3, 52, 2]
squared = list(map(lambda x: x * x, numbers))
print(f"Squared: {squared}")