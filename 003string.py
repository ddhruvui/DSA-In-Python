# Multi line string
exampleOfMultiLineString = """
Hi John,
I hope all is good
"""

print("exampleOfMultiLineString - ", exampleOfMultiLineString)

# ===============================================================


# String methods


nameOfAdmin = "Shleeji"

# length of string
print("length of Admin: ", len(nameOfAdmin))

# slice of string
print("Characters from 1 to len-3 :", nameOfAdmin[1:-3])


# escape sequence
method1 = '" hi Shleeji'
method2 = "how's life ?  \" said xyz"

# formatted string
print(f"Formatting string : {method1} {method2}")

# since its case sensitive, find will give -1 if we find shl directly
print("Index of shl: ", nameOfAdmin.lower().find("shl"))
