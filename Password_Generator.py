import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''
    
    # Combine all character pools
    all_characters = lowercase + uppercase + digits + special_chars
    
    # Ensure the password has at least one of each selected type
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_digits:
        password.append(random.choice(digits))
    if use_special_chars:
        password.append(random.choice(special_chars))
    
    # Fill the rest of the password length
    for _ in range(length - len(password)):
        password.append(random.choice(all_characters))
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    # Join the list into a string and return
    return ''.join(password)

# User input for password length and character types
try:
    length = int(input("Enter the desired password length (minimum 6): "))
    if length < 6:
        print("Password length should be at least 6.")
    else:
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'

        # Generate and display the password
        generated_password = generate_password(length, use_uppercase, use_digits, use_special_chars)
        print(f"Generated Password: {generated_password}")

except ValueError:
    print("Please enter a valid number for the password length.")
StopIteration