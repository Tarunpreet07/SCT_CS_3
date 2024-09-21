import re

def check_password_strength(password):
    strength_criteria = {
        "length": False,
        "uppercase": False,
        "lowercase": False,
        "digit": False,
        "special_char": False
    }

    # Check the length of the password
    if len(password) >= 8:
        strength_criteria["length"] = True

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength_criteria["uppercase"] = True

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength_criteria["lowercase"] = True

    # Check for digits
    if re.search(r'\d', password):
        strength_criteria["digit"] = True

    # Check for special characters
    if re.search(r'[\W_]', password):  # \W matches any non-word character (special characters)
        strength_criteria["special_char"] = True

    # Count the number of criteria met
    criteria_met = sum(strength_criteria.values())

    # Assign strength level based on criteria met
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Print detailed strength criteria
    print(f"Password Strength Criteria:")
    for criteria, met in strength_criteria.items():
        print(f"{criteria.title()}: {'Met' if met else 'Not Met'}")
    
    return strength


if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Your password strength is: {strength}")
