from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != 'admin':
            return "Access Denied: Admins only."
        result = func(user_role)
        return result
    return wrapper

@my_decorator
def sensitive_operation(user_role):
    return "Sensitive operation performed."
# Example usage
print(sensitive_operation('admin'))  # Should print: Sensitive operation performed.
print(sensitive_operation('guest'))  # Should print: Access Denied: Admins only.s
