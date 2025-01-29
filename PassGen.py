import random
import string

def generate_password(length=12, use_special_chars=True):
    # Define character sets
    # Get all ASCII letters (a-z and A-Z) from the string module
    letters = string.ascii_letters  # Includes both lowercase (a-z) and uppercase (A-Z) letters
    
    # Get all numeric digits (0-9) from the string module
    digits = string.digits  # Includes digits from 0 through 9
    
    # Define a custom set of special characters for password complexity
    # Includes commonly used symbols that are generally allowed in passwords
    # Note: Some systems may have restrictions on certain special characters
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/"  # Special characters for password generation
    # Create a pool of characters based on user preferences
    if use_special_chars:
        pool = letters + digits + special_chars
    else:
        pool = letters + digits

    #! Ensure the password length is at least 8 characters
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")

    #TODO Generate the password
    password = ''.join(random.choice(pool) for _ in range(length))

    #**** Ensure the password does not contain any spaces
    if ' ' in password:
        password = password.replace(' ', random.choice(pool))

    return password

# Example usage
if __name__ == "__main__":
    try:
        length = int(input("Enter the length of the password: "))
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        password = generate_password(length, use_special)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)