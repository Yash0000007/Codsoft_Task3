import random
import string

def generate_password(length):
    # Define character sets for password generation
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets for all characters
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure that the length is at least 8 characters
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    # Generate the password using random.choices
    password = ''.join(random.choices(all_characters, k=length))
    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired password length: "))
            password = generate_password(length)
            if password:
                print("Generated Password:", password)
            break
        except ValueError:
            print("Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
