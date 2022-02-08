def fibonacci_dinamico(n):
    if n == 0 or n == 1:
        return 1
    resultado = fibonacci_dinamico(n - 1) + fibonacci_dinamico(n - 2)

    return resultado

print(fibonacci_dinamico(4))
