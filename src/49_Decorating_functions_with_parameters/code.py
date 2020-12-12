import functools

users = [
    {"username": "jose", "access_level": "admin"},
    {"username": "joao", "access_level": "guest"}
]


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if users[1]["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {users[1]['username']}"

    return secure_function


@make_secure
def get_password(panel: str):
    if panel == "admin":
        return '1234'
    elif panel == "billing":
        return "super_secure_password"


print(get_password("billing"))
print(get_password.__name__)
