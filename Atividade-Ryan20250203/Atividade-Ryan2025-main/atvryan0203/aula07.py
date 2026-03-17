def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fatorial(5))
print(fibonacci(6))
