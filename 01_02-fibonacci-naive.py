def fib(n):
    # Ideally check for negative n and throw an exception, but for the purposes
    # of this demonstration, not needed.
    if n == 0: return 1
    if n == 1: return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    import timeit

    for n in [10, 20, 30]:
        duration = timeit.timeit(f'fib({n})', number=100, globals=globals())
        print(f'fib({n:3}) took {duration:8.5f}s')
