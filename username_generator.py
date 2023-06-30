import random

def generate_username(first_name, last_name, email_adress):
    username = first_name[0] + last_name + email_adress[1] + str(random.randint(100, 999))
    return username.upper()  # Convert username to lowercase

# User input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email_adress = input("Enter your email adress:")

# Generate username
username = generate_username(first_name, last_name, email_adress)
print("Generated username:", username)
