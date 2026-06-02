

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''

    if n % 2 == 0:
        return False
    else:
        return True


# Base-2 Representation of 42: 101010

# Right-to-left method builds binary by returning 0 as right-most value if base-10
# number is even, and 1 as right-most value if base-10 number is odd.
# Eliminating right-most bit is equivalent to performing int division of 2: int(n/2)


def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    
    if n == 0:
        return ''
    
    else:
        if isOdd(n) == True:
            s = str(1)              # Concatenate base-2 of int(n/2) with '1' if n is odd
        if isOdd(n) == False:
            s = str(0)              # '0' if n is even
        return numToBinary(n // 2) + s


# Let y denote int(n/2). Let r denote base-2 representation of y.
# Given r, base-2 representation of n can be found by concatenating r with '1' if n is odd,
# and r with '0' if n is even. Concatenating '0' is equivalent to (y*2); concatenating '1'
# is equivalent to (y*2)+1.


def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.'''
    
    if s == '':
        return 0

    else:
        if s[-1] == '1':
            return (binaryToNum(s[:-1]) * 2) + 1
        if s[-1] == '0':
            return (binaryToNum(s[:-1]) * 2)


def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    
    new = numToBinary(binaryToNum(s) + 1)

    if len(new) < 8:
        missing = 8 - len(new)
        new = (missing * '0') + new         # Add string of missing 0's if length is < 8
    if len(new) > 8:
        new = new[-8:]                      # Return only last 8 bits if length is > 8

    return new


def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''

    print(s)

    if n == 0:
        return

    else:
        count(increment(s), n-1)


# Ternary Representation for 59: 2012
# 59%3 is 2, so right-most value is 2. (59//3)%3 is 1, so concatenate '1' to '2' for current
# string of '12'. Next, ((59//3)//3)%3 is 0, so now '012'. Last recursive call concatenates
# another '2'. Final result is '2012'. 


def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    
    if n == 0:
        return ''
    
    else:
        if n % 3 == 0:                      # Concatenate '0' if remainder is 0
            s = str(0)
        if n % 3 == 1:                      # '1' if remainder is 1
            s = str(1)
        if n % 3 == 2:                      # '2' if remainder is 2
            s = str(2)
        return numToTernary(n // 3) + s


def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    
    if s == '':
        return 0

    else:
        if s[-1] == '2':
            return (ternaryToNum(s[:-1]) * 3) + 2
        if s[-1] == '1':
            return (ternaryToNum(s[:-1]) * 3) + 1
        if s[-1] == '0':
            return (ternaryToNum(s[:-1]) * 3)


