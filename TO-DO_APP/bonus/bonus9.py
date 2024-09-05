# Checking the strength of the password

password = input("Enter new password: ")

result = {}

# Special characters set
special_characters = "!@#$%^&*()-+?_=,<>/"

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
# checking for special characters
special_char = False
for char in password:
    if char in special_characters:
        special_char = True

result["special_char"] = special_char

# --------------------------------
if all(result.values()):
    print("Strong Password")
else:
    print("Weak password")
