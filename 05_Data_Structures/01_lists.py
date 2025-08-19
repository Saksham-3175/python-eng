list_1 = [1, 2, 3, 4, 5]
num = [6, 7, 8]
list_2 = ["one", "two", "three", "four", "five"]

# print(list_1)
list_1.extend(num)
# print(list_1)

#list_append = list_1.append(num) # append expects only a single integer.


records = [["mark", 67], ["henry", 23], ["Mike", 42]]
print(records[0][1])

scores = [score[1] for score in records]
print(scores)
# scores = [for score in records[]]