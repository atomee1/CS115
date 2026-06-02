words = []

def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoisation to speed up the process.'''
    if (first, second) in words:
        return words[(first, second)]
    elif first == "" or second == "":
        words[(first, second)] = 0
        return 0
    elif first[0] == second[0]:
        result = fastED(first[1:], second[1:])
        words[(first, second)] = result
        return result
    else:
        substitution = 1 + fastED(first[1:], second[1:])
        deletion = 1 + fastED(first[1:], second)
        insertion = 1 + fastED(first, second[1:])
        result = min(substitution, deletion, insertion)
        memo[(first, second)] = result
        return result
