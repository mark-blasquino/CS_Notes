def fibonacci(n):
    if n <= 1:
        return 1
    else:
        n_minus_1 = fibonacci(n-1)
        n_minus_2 = fibonacci(n-2)
        return n_minus_1 + n_minus_2

print(fibonacci(4))