mlist = ["string", 23, 42.22, "type"]

##append: add one item at the end
mlist.append("object")
# print(mlist)

##extend(iterable): extends the list from the iterable
list2 = [23, 42, 90, 10]
mlist.extend(list2)
# print(mlist)

##insert: add item at a given position(i, x) i-> index
list2.insert(3, 27)
# print(list2)

##remove: remove the first item
list2.remove(23)
# print(list2)

##pop: remove the item at a given index(passed as a list)
mlist.pop(2)
# print(mlist)# 42.22 is popped

##clear: removes all the items
list3 = mlist.copy()
# print(list3)
list3.clear()
# print(list3)

##index: returns the index of an item.. 23-> item, 2(start index), 5(stop index) 
# print(mlist)
# print(mlist.index(23, 2, 5))

##count: no. of times x is repeated
# print(mlist.count(23))

##sort: sorts in-place and **returns None**
list4 = list2.copy()
# print(list4)
list4.sort()
# print(list4)

list4.sort(reverse=True)
# print(list4)
#key parameter:
words = ['apple', 'fig', 'banana']
# print(f'words before: {words}')
words.sort(key=len)
# print(f'by length: {words}')

words2 = ["bob", "Alice", "carten"]
words2.sort(key=str.lower)
# print(f'Case-insensitive: {words2}')

#sorting a list of tuples by the second element
tuples = [("a", 3), ("b", 1), ("c", 2)]
# print(f"\n{tuples}")
tuples.sort(key=lambda x: x[1])
# print(f"\nTuples by second element: {tuples}")

#sorting list of dicts by a field
people = [{"name":"bob", "age":30}, {"name":"carol", "age": 33}, {"name":"vincent", "age":23}]
# print(f"\n{people}")
people.sort(key = lambda p: p['age'])
# print(f"\nPeople by age: {people}")

#using operator.itemgetter (slightly faster then lambda)
from operator import itemgetter
tuples2 = [("x", 10), ("y", 2), ("z", 5)]
# print(f"\n{tuples2}")
tuples2.sort(key=itemgetter(1), reverse=True)
# print(f"\nitemgetter reverse: {tuples2}")

# print(tuples2)
# tuples2.reverse()
# print(tuples2)


def using_as_stacks():
    stack = [2, 4, 5]
    print(f"Stack: {stack}")
    nums = [8, 7]
    print(f"Nums: {nums}")
    stack.extend(nums)
    print(f"Stacks.Extend: {stack}")

    return stack

# using_as_stacks()

#queues
from collections import deque
def using_as_queues():
    queue = deque(['Eric', 'John', 'Michael'])
    print(f"Queue: {queue}")

    names = ['Terry', 'Bob']
    print(f"Names: {names}")

    queue.extend(names)
    print(f"Extended Names: {queue}")

    queue.popleft()
    print(f"Pop Left: {queue}")

    queue.pop()
    print(f"Pop queue: {queue}")
    
    return queue

using_as_queues()