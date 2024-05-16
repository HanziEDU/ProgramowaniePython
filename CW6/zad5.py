import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Czas wykonania funkcji {func.__name__}: {end_time - start_time} sekund")
        return result
    return wrapper

@measure_time
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

@measure_time
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_recursive(5))
print(factorial_iterative(5))