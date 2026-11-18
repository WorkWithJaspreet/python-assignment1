def check_length(pwd):
    return len(pwd) >= 8

def has_uppercase(pwd):
    for ch in pwd:
        if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return True
    return False

def has_lowercase(pwd):
    for ch in pwd:
        if ch in "abcdefghijklmnopqrstuvwxyz":
            return True
    return False

def has_digit(pwd):
    for ch in pwd:
        if ch in "0123456789":
            return True
    return False

def has_special(pwd):
    for ch in pwd:
        if ch in "!@#$%^&*()_+-=[]{}|;:',.<>?/~`":
            return True
    return False

def has_no_space(pwd):
    return " " not in pwd

def validate_password(pwd):
    errors = []
    if not check_length(pwd):
        errors.append("Password must contain at least 8 characters.")
    if not has_uppercase(pwd):
        errors.append("Password must contain an uppercase alphabet.")
    if not has_lowercase(pwd):
        errors.append("Password must contain a lowercase alphabet.")
    if not has_digit(pwd):
        errors.append("Password must contain a digit.")
    if not has_special(pwd):
        errors.append("Password must contain a special character.")
    if not has_no_space(pwd):
        errors.append("Password must not contain any space.")
    return errors

print("===== SECURE EMPLOYEE ACCOUNT SYSTEM =====")
num_accounts = int(input("\nEnter number of accounts to create: "))

accounts = {}

for i in range(num_accounts):
    print(f"\n--- Account {i + 1} ---")
    username = input("\nEnter username: ")

    while True:
        password = input("Enter password: ")
        errors = validate_password(password)

        if len(errors) == 0:
            break
        else:
            print("\nPassword rejected!")
            for err in errors:
                print(err)
            print()

    while True:
        confirm_password = input("Confirm password: ")
        if password == confirm_password:
            accounts[username] = password
            print("\nAccount created successfully!")
            break
        else:
            print("Passwords do not match. Please enter the confirm password again.")

print("\n===== EMPLOYEE LOGIN =====")

max_attempts = 5
attempts = 0

while attempts < max_attempts:
    login_username = input("\nEnter username: ")
    login_password = input("Enter password: ")

    if login_username in accounts and accounts[login_username] == login_password:
        print("\nLogin successful!")
        print(f"Welcome {login_username}")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print("\nInvalid username or password.")
        if remaining > 0:
            print(f"Attempts remaining: {remaining}")
        else:
            print("\nAccess Denied!")
            print("Maximum login attempts exceeded.")