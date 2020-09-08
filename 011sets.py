# set is unordered and unindexed
# no duplicates

first = [1,1,2,3,4]
first = set(first)

second = {1,5}

# get union of 2 set -
print( first | second)

# intersection of 2 sets -
print( first & second)

# values not common in 2 sets - 
print( first ^ second)

# values in first set not in 2nd set -
print(first - second)