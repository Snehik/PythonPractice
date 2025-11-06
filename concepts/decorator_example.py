from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before calling the function.")
        result = func(*args, **kwargs)
        print("After calling the function.")
        return result
    return wrapper
@my_decorator
def say_hello(name):
    """Greets a person by name."""
    print(f"Hello, {name}!")    
    return f"Greeted {name}"
# Example usage
if __name__ == "__main__":
    greeting = say_hello("Alice")
    print(greeting)
    print(f"Function name: {say_hello.__name__}")
    print(f"Function docstring: {say_hello.__doc__}")   
    