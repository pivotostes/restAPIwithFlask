import functools

users = {"username": "jose", "access_level": "admin"}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function():
            if users["access_level"] == access_level:
                return func()
            else:
                return f"No {access_level} permissions for {users['username']}"

        return secure_function
    return decorator


@make_secure("admin")
def get_admin_password():
    return 'admin: 1234'


@make_secure("guest")
def get_dashboard_password():
    return 'user: user_password'


print(get_admin_password())
print(get_dashboard_password())

users = {"username": "joao", "access_level": "guest"}
print(get_admin_password())
print(get_dashboard_password())
