import sys

def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)



if __name__ == '__main__':
    sys.setrecursionlimit(10002)
    n = int(input('Escoge un numero: '))
    print(fibonacci_recursivo(n))