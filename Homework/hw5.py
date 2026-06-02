
lucas_memo = {}
change_memo = {}


def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    
    if (n) in lucas_memo:
        return lucas_memo[(n)]
    
    elif n == 0:
        lucas_memo[(n)] = 2
        return lucas_memo[(n)]
    
    elif n == 1:
        lucas_memo[(n)] = 1
        return lucas_memo[(n)]
    
    else:
        lucas_memo[(n)] = fast_lucas(n - 1) + fast_lucas(n - 2)
        return lucas_memo[(n)]


def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''

    if (amount) in change_memo:
        return change_memo[(amount)]
    
    elif amount == 0:
        change_memo[(amount)] = 0
        return change_memo[(amount)]
    
    elif amount < 0 or coins == []:
        return float("inf")
    
    lose = fast_change(amount, coins[1:])
    use = 1 + fast_change((amount - coins[0]), coins)
    change_memo[(amount)] = min(lose, use)
    return change_memo[(amount)]


# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))


