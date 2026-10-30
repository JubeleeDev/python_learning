
from functools import wraps
from collections.abc import Callable

def log_call(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"name={func.__name__}, args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"result = {result}")

        return result

    return wrapper

@log_call
def sum_numbers(a: int, b: int) -> int:
    return a + b

@log_call
def say_age(name: str, age: int = 0, description: str = "no description") -> str:
    return f"Hello, {name}. Your age is {age}. {description}"

if __name__ == "__main__":
    print(sum_numbers(5, 10))
    print(say_age(name="Alex", description="Test description"))
    print(sum_numbers.__name__)