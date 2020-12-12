import functools

users = [
    {"username": "jose", "access_level": "admin"},
    {"username": "joao", "access_level": "guest"}
]


def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if users[1]["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {users[1]['username']}"

    return secure_function


@make_secure
def get_admin_password() -> str:
    return '1234'


print(get_admin_password())
print(get_admin_password.__name__)
