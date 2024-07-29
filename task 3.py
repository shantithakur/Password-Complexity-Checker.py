import re

def password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters.")
    else:
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should have at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should have at least one lowercase letter.")

    # Check for numbers
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Password should have at least one number.")

    # Check for special characters
    if re.search(r"\W", password):
        strength += 1
    else:
        feedback.append("Password should have at least one special character.")

    # Determine password strength
    if strength <= 2:
        password_strength = "Weak"
    elif strength <= 4:
        password_strength = "Medium"
    else:
        password_strength = "Strong"

    return password_strength, feedback

def main():
    password = input("Enter a password: ")
    strength, feedback = password_strength(password)

    print(f"Password strength: {strength}")
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(item)
if __name__ == "__main__":
        main()