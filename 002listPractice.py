# List does not have a specific data type like array
arr = ["abc", 1,2,3,4,5,6,7]
print ("Original array :",arr)


# Inserting elements

arr1 = [8,9,10]
arr += arr1
print ("New arr after adding arr1:",arr)

arr2 = [11,12,13,14]
arr.extend(arr2)
print ("New arr after adding arr2:",arr)

arr.append(15)
print ("Current list after appending 15:", arr)

arr.insert(1,0)
print ("Current list after inserting 0 at 1:", arr)



print ("Current list:", arr)
print ("Length of arr :", len(arr))

print ("Number of times 15 is in arr:", arr.count(15))

print ("Element removed on pop:", arr.pop())

arr.remove('abc') # Removes item, the value is not the position
print ("New arr after remove('abc'):", arr)

del arr[0]
print ("New arr after del(0):", arr)
# del arr will delete array and if we try to access it will raise error
# arr.clear() will remove all elements at once



#Accessing array element
print ("Current list:", arr)
print ("First element:", arr[0])
print ("2nd to last element:", arr[1:])
print ("2nd and 3rd element:", arr[1:3]) # Remember the last index is ignored
print ("Last element:", arr[-1])
print ("Last 3 elements:", arr[-3:])
print ("Reversed array:",arr[::-1])



# To copy 1 list to other -
list1 = arr # This copies just the address of arr
list2 = arr.copy()
arr.append(8)
print ("Copied List 1: ", list1)
print ("Copied List 2: ", list2)


#loop through array
for x in arr :
    pass

# check if item exists
if 7 in arr:
    print ("7 exists in array")
if 8 in arr:
    print ("8 exists in array")