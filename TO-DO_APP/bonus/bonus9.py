# Checking the strength of the password

password = input("Enter new password: ")


# Initialize result variables
has_digit = False
has_upper_case = False
has_special_char = False
has_lower_case = False


special_characters = "!@#$%^&*()-+?_=,<>/"


# Asking user to customize special characters:
custom_special_characters = input("Enter allowed special characters (leave empty for default): ")
if not custom_special_characters:
    custom_special_characters = special_characters


# Check conditions in one loop
for char in password:
    if char.isdigit():
        has_digit = True
    elif char.isupper():
        has_upper_case = True
    elif char.islower():  # Check for lowercase
        has_lower_case = True
    elif char in custom_special_characters:
        has_special_char = True

    # Early exit if all conditions are met
    if has_digit and has_upper_case and has_lower_case and has_special_char:
        break

# Checking the length after the loop
is_valid_length = len(password) >= 8

# Final check and feedback
if is_valid_length and has_digit and has_upper_case and has_lower_case and has_special_char:
    print("Strong Password")
else:
    print("Weak Password. Issues with:")
    if not is_valid_length:
        print("- Password should be at least 8 characters long.")
    if not has_digit:
        print("- Password should contain at least one digit.")
    if not has_upper_case:
        print("- Password should contain at least one uppercase letter.")
    if not has_lower_case:
        print("- Password should contain at least one lowercase letter.")  # Feedback for lowercase
    if not has_special_char:
        print(f"- Password should contain at least one special character from the set: {custom_special_characters}.")