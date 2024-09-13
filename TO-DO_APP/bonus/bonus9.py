# Checking the strength of the password

password = input("Enter new password: ")

# Prompt user to customize special characters
custom_special_characters = input("Enter allowed special characters (leave empty for default set): ")
if not custom_special_characters:
    custom_special_characters = "!@#$%^&*()-+?_=,<>/"

# Initialize result variables
digit_count = 0  # Count of digits
has_upper_case = False
has_lower_case = False
has_special_char = False

# Minimum digit requirement
min_digits = 2  # Require at least 2 digits

# Check conditions in one loop
for char in password:
    if char.isdigit():
        digit_count += 1  # Increment digit count
    elif char.isupper():
        has_upper_case = True
    elif char.islower():
        has_lower_case = True
    elif char in custom_special_characters:
        has_special_char = True

    # Early exit if all conditions are met
    if digit_count >= min_digits and has_upper_case and has_lower_case and has_special_char:
        break

# Checking the length after the loop
is_valid_length = len(password) >= 8
has_min_digits = digit_count >= min_digits  # Check if the number of digits meets the requirement

# Final check and feedback
if is_valid_length and has_min_digits and has_upper_case and has_lower_case and has_special_char:
    print("Strong Password")
else:
    print("Weak Password. Issues with:")
    if not is_valid_length:
        print("- Password should be at least 8 characters long.")
    if not has_min_digits:
        print(f"- Password should contain at least {min_digits} digits.")
    if not has_upper_case:
        print("- Password should contain at least one uppercase letter.")
    if not has_lower_case:
        print("- Password should contain at least one lowercase letter.")
    if not has_special_char:
        print(f"- Password should contain at least one special character from the set: {custom_special_characters}.")
