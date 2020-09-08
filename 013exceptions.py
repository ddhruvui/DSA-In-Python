from timeit import timeit

try:
    age=int(input("Age:"))
    xfactor = 10/ age
except (ValueError, ZeroDivisionError): # as ex:
    print("age entered is invalid")
    # print(ex)
    # print(type(ex))
# else will only be executed if there is no exception
else:
    print("Gotcha!!!")
#finally is executed at very end irrespective of error has occured or not
finally:
    print("terminating database connection....")


code1="""
def calculate_xfactor(age):
    if(age<=0):
        raise ValueError("age should be greater then 0")
    return 10/age

try:
    calculate_xfactor(0)
except ValueError as error:
    pass
"""

code2="""
def calculate_xfactor(age):
    if(age<=0):
        return None
    return 10/age

try:
    calculate_xfactor(0)
except ValueError as error:
    pass
"""

print("Code 1:", timeit(code1, number =10000))
print("Code 2:", timeit(code2, number =10000))