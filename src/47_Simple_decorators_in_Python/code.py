users = [
    {"username": "jose", "access_level": "admin"},
    {"username": "joao", "access_level": "guest"}
]


def get_admin_password() -> str:
    return '1234'


def make_secure(func):
    def secure_function():
        if users[0]["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {users[0]['username']}"

    return secure_function


get_admin_password = make_secure(get_admin_password)
print(get_admin_password())
