def register_user(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    users[username] = {"password": password, "vehicles": [], "notifications": []}
    print("User registered successfully!")
