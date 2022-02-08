import hashlib
from time import time

data_memo = {}


def memoization(func):
    def func_wrapper(*kwargs):
        _hash = hashlib.md5((func.__name__+str(kwargs)).encode()).hexdigest()
        if _hash in data_memo:
            return data_memo[_hash]
        _result = func(*kwargs)
        data_memo[_hash] = _result
        return _result
    return func_wrapper


@memoization
def fibonacci_recursive_memo(n):
    return 1 if n == 0 or n == 1 else fibonacci_recursive_memo(n-1) + fibonacci_recursive_memo(n-2)


def fibonacci_recursive(n):
    return 1 if n == 0 or n == 1 else fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


if __name__ == '__main__':
    n = int(input('chose a number: '))
    start = time()
    result = fibonacci_recursive_memo(n)
    end = time()
    print(f"result with memo {result} in {end-start}")
    start = time()
    result = fibonacci_recursive(n)
    end = time()
    print(f"result without memo {result} in {end-start}")

