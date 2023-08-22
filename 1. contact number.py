import re

def is_valid_contact_number(contact_number):
    # Regular expression pattern to match valid contact numbers
    pattern = r'^(\+?\d{0,2})?[-. ]?\(?\d{2,}\)?[-. ]?\d{3,}[-. ]?\d{4}$'

    # Check if the contact number matches the pattern
    if re.match(pattern, contact_number):
        return True
    else:
        return False

# Test cases
contact_numbers = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890"
]

for number in contact_numbers:
    if is_valid_contact_number(number):
        print(f"{number} is a valid contact number.")
    else:
        print(f"{number} is an invalid contact number.")