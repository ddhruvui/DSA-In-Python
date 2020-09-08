def printName(name, surname):
    return(f"Hi {name} {surname}")


nameToBePrinted = printName("Dhruv", surname="Desai")
print(nameToBePrinted)


def sumOfIntegers(*integers):
    sum = 0
    for number in integers:
        sum += number
    print("sum of numbers is:", number)


sumOfIntegers(1, 2, 3, 4)


def userDetails(**user):
    print("user id is:", user["id"])


userDetails(id=1)

# modifying global variable
# its a bad practice
message = "old"


def changeMsg():
    global message
    message = "new"


changeMsg()
print(message)


def fizzBuzz(num):
    if not num % 15:
        return "FizzBuzz"
    elif not num % 3:
        return "fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


print(fizzBuzz(7))
