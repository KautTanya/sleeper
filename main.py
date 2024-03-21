"""sleeper"""
from time import sleep


def sleeper(n):
    """sleeper"""
    def decorator(func):
        """sleeper"""
        def wrapper(*args, **kwargs):
            """sleeper"""
            sleep(n)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@sleeper(5)
def add_numbers(a, b):
    """example"""
    return a + b


print(add_numbers(8, 7))
