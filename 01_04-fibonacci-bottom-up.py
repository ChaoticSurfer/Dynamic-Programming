def fib(n):
    a = 1  # f(i - 2)
    b = 1  # f(i - 1)
    for i in range(2, n + 1):  # end of range is exclusive
        # the old "a" is no longer accessible after this
        a, b = b, a + b

    return b


