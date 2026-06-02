
def factorial(n):
    # nList = list (range (1, n+1))
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)