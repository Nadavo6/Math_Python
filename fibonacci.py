def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    return fib_series

n = 10
print("Fibonacci sequence of length", n, "is:", fibonacci(n))