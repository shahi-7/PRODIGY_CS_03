import re

# Function to check password complexity
def check_password_complexity(password):
    # Initialize a strength counter
    strength = 0
    
    # Criteria 1: Length check (at least 8 characters)
    if len(password) >= 8:
        strength += 1
    else:
        print("Password must be at least 8 characters long.")
    
    # Criteria 2: Uppercase letter check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        print("Password must contain at least one uppercase letter.")
    
    # Criteria 3: Lowercase letter check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        print("Password must contain at least one lowercase letter.")
    
    # Criteria 4: Number check
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        print("Password must contain at least one number.")
    
    # Criteria 5: Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        print("Password must contain at least one special character.")
    
    # Provide feedback based on strength score
    if strength == 5:
        print("Password is very strong!")
    elif strength == 4:
        print("Password is strong.")
    elif strength == 3:
        print("Password is medium.")
    else:
        print("Password is weak.")

# Main function to take user input and check password complexity
def main():
    password = input("Enter a password to check: ")
    check_password_complexity(password)

if __name__ == "__main__":
    main()
