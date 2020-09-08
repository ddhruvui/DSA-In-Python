'''
    Input is always string
    int(), bool(), float() and str() are available for type conversion
'''
x = input("x: ")
y = int(x)+1
print(f"x: {x}, y: {y}")

'''
bool is false for Falsy,"",0 and None
else always True i.e. even for "0"
'''
z = bool(x)
print(z)
