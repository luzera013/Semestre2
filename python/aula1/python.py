def fatorial_rec(n):
    if n == 0:
        return 1
    return n * fatorial_rec(n - 1)

fatorial_rec(150)