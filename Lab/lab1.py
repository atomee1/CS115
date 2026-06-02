
from math import factorial
from functools import reduce

def inverse(x):
    reciprocal = 1/x
    return reciprocal
    pass

def e(n):
    list1 = list (range (1, n + 1))
    factorial_list = list (map (factorial, list1))
    reciprocal_list = list (map (inverse, factorial_list))
    e = 1 + sum(reciprocal_list)
    return e
    pass
