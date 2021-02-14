def fib(n, cache=None):
    if n == 0: return 1
    if n == 1: return 1

    if cache is None: cache = {}
    if n in cache: return cache[n]

    result = fib(n - 1, cache) + fib(n - 2, cache)
    cache[n] = result
    return result


if __name__ == '__main__':
    import timeit

    for n in [10, 20, 30, 100]:
        duration = timeit.timeit(f'fib({n})', number=100, globals=globals())
        print(f'fib({n:3}) took {duration:8.5f}s')
