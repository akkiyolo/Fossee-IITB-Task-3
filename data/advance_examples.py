# Advanced Examples

# Infinite recursion due to poor stopping condition
def power(base, exp):
    if exp >= 0:  # Wrong base case
        return 1
    return base * power(base, exp-1)

# Misuse of classes: forgetting _init_
class Student:
    name
    def greet(self):
        print("Hello", self.name)

# Incorrect use of decorators
def log(func):
    def wrapper(*args, **kwargs):
        print("Calling function")
        return func()
    return wrapper

@log
def add(a, b):
    return a + b  # Will fail, args not passed