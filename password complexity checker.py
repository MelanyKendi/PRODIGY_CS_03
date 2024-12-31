import re

def check_password_strength(password):
    # Initialize strength criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_character_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Calculate total score
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_character_criteria])

    # Provide feedback
    if score == 5:
        return "Strong Password: Meets all criteria!"
    elif score >= 3:
        return "Moderate Password: Consider adding more complexity."
    else:
        return "Weak Password: Does not meet enough criteria."

# Example usage
password = input("Enter your password: ")
result = check_password_strength(password)
print(result)
