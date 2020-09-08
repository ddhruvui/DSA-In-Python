# To create list of 100 zero's
listOfZeros = [0]*100

listOf0to20 = list(range(21))
# print list in reverse order
# print(listOf0to20[::-1])

chars = list("Hello world")
lengthOfChars = len(chars)

# list unpacking
numbers = [1,2,3,4,5,6, 7]
first, second, *other, last = numbers
# js ... is replaced by * for rest and spread
# rest is pcking and spread is unpacking sort of

# to just print value and not index
# for number in numbers:
    #print(number)

# to print both index and value - 
#for index, character in enumerate(chars):
#   print(index, character)

# to sort
numbers = [5,3,7,2,8]
numbers.sort()
# numbers.sort(reverse = True)
# sort affects original array
# sorted creates a new array and makes changes
# print(sorted(numbers, reverse = True))


items = [
    ("prod1", 10),
    ("prod2", 5),
    ("prod3", 80),
    ("prod4", 75),
]
items.sort(key = lambda item : item[1])

prices = list(map(lambda item : item[1], items)) 
# List comprehension
# Produces same result as map and filter
prices = [item[1] for item in items]

expensiveProducts = list(filter(lambda item : item[1] > 50, items))
expensiveProducts = [item for item in items if item[1]>50]
print(expensiveProducts)

thislist = ["apple", "banana" , "orange", "banana"]
thislist.remove("c")
print(thislist)