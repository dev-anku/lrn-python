def fib_iter(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


def fib_rec(n):
    if n <= 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


print(fib_iter(100))
print(fib_rec(19))
