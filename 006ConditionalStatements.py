temperature = 35

if temperature > 30:
    print("Its hot today")
elif temperature > 15:
    print("Wether today is awesome")
else:
    print("Its cold")

# ============================================================

# Ternary operator
age = 15
message = "Eligible" if age >= 18 else "Not Elegible"
print(message)

# ============================================================

# Logical - and / or / not

highIncome = False
goodCredit = False
student = False

if highIncome and goodCredit:
    print("Elegible for credit card")
elif goodCredit and student:
    print("Eligible with limited credit limit")
elif highIncome or goodCredit or not student:
    print("Consider for a pre-check")
else:
    print("Not eligible")
