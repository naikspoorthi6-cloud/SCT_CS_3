import string

# Get password from the user
password = input("Enter your password: ")

# Initialize the strength score
score = 0

# Check password length
if len(password) >= 8:
    score += 1

# Check for uppercase letters
if any(char.isupper() for char in password):
    score += 1

# Check for lowercase letters
if any(char.islower() for char in password):
    score += 1

# Check for numbers
if any(char.isdigit() for char in password):
    score += 1

# Check for special characters
if any(char in string.punctuation for char in password):
    score += 1

# Display password strength
if score <= 2:
    print("Password Strength: WEAK")

elif score <= 4:
    print("Password Strength: MODERATE")

else:
    print("Password Strength: STRONG")