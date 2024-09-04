# Checking the strength of the password

password = input("Enter new password: ")

result = {}


# --------------------------------
# checking for length
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False


# --------------------------------
# checking for digits
digit = False
for char in password:
    if char.isdigit():
        digit = True

result["digit"] = digit


# --------------------------------
# checking for upper case
upper_case = False
for char in password:
    if char.isupper():
        upper_case = True

result["upper_case"] = upper_case


# --------------------------------
if all(result.values()):
    print("Strong Password")
else:
    print("Weak password")
