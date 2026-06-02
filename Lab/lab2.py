
def length(L):
    """ Finds length of list L """
    if L == []:
        # Base case: If list is empty, return 0
        return 0
    return 1 + length(L[1:])


def dot(L, K):
    """ Calculates the dot product of lists L and K (vectors) """
    if length(L) != length(K):
        # Returns 0 if lists are different lengths
        print ("Invalid input.")
    elif L == [] or K == []:
        # Base case: If list is empty, return 0.
        return 0
    else:
        rest = dot(L[1:], K[1:])
        return (L[0]*K[0]) + rest


def explode(S):
    """ Takes string S and returns a list of the characters """
    sList = list(S)         # Convert string S into list
    if sList == []:         # Base case: If list is empty, return 0
        return []
    return list(S[0]) + explode(S[1:])


def ind(e, L):
    """ Returns index at which e is first found in L.
        If e is not in L, return an integer == len(L) """
    if L == [] or L == "":
        return 0
    elif e == L[0]:
        return 0
    else:
        pos = 1 + ind(e, L[1:])
        return pos


def removeAll(e, L):
    """ Removes all elements e in list L (e must be top-level) """
    if L == []:
        return []                           # If list is empty, return empty
    elif e == L[0]:
        return removeAll(e, L[1:])          # Do not add element to list
    else:
        return [L[0]] + removeAll(e, L[1:]) # Add element to list


def even(n):
    """ Returns True if input is even; False otherwise """
    # Predicate for myFilter function
    if n%2 == 0:
        return True
    return False

    
def myFilter(f, L):
    """ Returns new list containing elements in L that return True """
    if L == []:
        return []
    elif f(L[0]) == False:
        return myFilter(f, L[1:])           # If odd, do not add to list
    else:
        return [L[0]] + myFilter(f, L[1:])  # If even, add to list


def deepReverse(L):
    """ Reverses list L """
    if L == []:
        return []
    elif isinstance(L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])] # Pass list through function
    else:
        return deepReverse(L[1:]) + [L[0]]              # Add non-list element

