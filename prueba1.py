def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado
        return resultado

