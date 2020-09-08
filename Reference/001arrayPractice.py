import array as array

arr = array.array('i',[1,2,3])
print ("Original:",arr)

arr.append(4)
print ("After appending 4:",arr)

new_arr = array.array('i',[7,8,9])
arr.extend(new_arr)
print ("After extending new array in old one :",arr)

arr.insert(0,5)
print ("After inserting 5 at position 0:",arr)

arr.insert(0,5)
print ("After inserting 5 again at position 0:",arr)





print("Type of array:",arr.typecode)

print("Length of every element in bytes:",arr.itemsize)




print("Length of array:",arr.buffer_info()[1])

print("Number of occurence of 5:",arr.count(5))

print("First 5 is at:", arr.index(5))

print ("Removed element for pop:",arr.pop())
print ("Array after removal:", arr)

print ("Removed element for pop(0):",arr.pop(0))
print ("Array after removal:", arr)

#Removes first occurenece of element in array
arr.remove(4)




# This method of reversing is called slicing and does not affect original arr
print("Reversed array : ", arr[::-1])

# Reverses original arr
arr.reverse()
print("Reversed array : ", arr)