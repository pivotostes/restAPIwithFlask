users = [
    (101, "Bob", "password"),
    (102, "Ralph", "12345"),
    (103, "Peter", "pass123"),
    (104, "John", "longpass12345"),
    (105, "Dan", "dan1234"),
]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ").capitalize()
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect. Please check your password.")

