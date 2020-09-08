print("Simple for loop : ")
for x in range(5):
    print(x)


print("For loop with other args and step of 2: ")
for x in range(0, 5, 2):
    print(x)

# Breaking for loop
success = True
for x in range(0, 5, 2):
    print("Attempt")
    if success:
        print("Successfull")
        break

# else executes if break is not executed
success = False
for x in range(0, 5, 2):
    print("Attempt")
    if success:
        print("Successfull")
        break
else:
    print("Failed")

# list, string are also iterable apart from range

print("Values of list:")
for x in [1, 2, 3]:
    print(x)

print("Alphabets in word Python:")
for x in "Python":
    print(x)


# while loop
print("While loop o/p:")
num = 100
while num >= 2:
    num //= 2
    print(num)
