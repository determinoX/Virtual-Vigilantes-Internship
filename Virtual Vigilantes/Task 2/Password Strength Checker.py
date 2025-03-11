import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")

    # Ensure index is within bounds
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong", "Excellent"]
    strength_index = min(strength, len(strength_levels) - 1)

    print(f"Password Strength: {strength_levels[strength_index]}")
    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print(f"- {tip}")

# Get user input
password = input("Enter your password: ")
check_password_strength(password)
