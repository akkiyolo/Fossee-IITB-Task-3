# Intermediate Examples

# Factorial with missing base case
def factorial(n):
    return n * factorial(n-1)

# Fibonacci missing n==1 case
def fibonacci(n):
    if n == 0: return 0
    return fibonacci(n-2) + fibonacci(n-1)