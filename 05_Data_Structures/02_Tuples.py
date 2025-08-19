tup_1 = (23, 342, 6)
tup_2 = (5,)  #For a single element tuple, comma is required

#Accessing Tuples:
# print(tup_1[0])

#Tuple Unpacking:
a, b, c = tup_1
# print(a, b, c)
# print(type(a))

#Common Methods(since immutable, less methods)
#1. Count-> The total count of an element
#2. index-> The first occurence of an element
mytup = (1, 6, 2, 4, 6, 2, 5, 3)

print(f"The count of 6 in mytup is: {mytup.count(6)}")
print(f"The first occurence of 5 in mytup is at index {mytup.index(5)}")

#Why tuples over lists?
print("Faster than Lists")
print("Used as dict keys")
print("Safe from modifications")

# print(mytup[0:3])
# print(mytup[0:4:2])




'''
Data Structure no. 2-> Tuples

mytup = (1, 2, 3)
type(mytup)

#Indexing-> Just like Lists
mytup[0]

#Slicing-> Just like Lists
mytup[0:4:2]

#Methods(2 since it's immutable)
#1. Count
code

#2. Index
code

'''