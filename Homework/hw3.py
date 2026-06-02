
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def concatenateList(L, coin):
    return [L[0] + 1, L[1] + [coin]]

def compare(L1, L2):
    if L1[0] < L2[0]:
        return L1
    return L2

def giveChange(amount, coins):
    """ Returns minimum number of coins required for given amount,
        as well as a list of the coins in that solution """

    if amount == 0:
        return [0, []]

    if amount < 0 or coins == []:
        return [float("inf"), []]

    else:
        if coins[0] > amount:
            return giveChange(amount, coins[1:])
        else:
            lose = giveChange(amount, coins[1:])
            use =  concatenateList(giveChange(amount - coins[0] , coins[0:]), coins[0]) 
            return compare(lose, use)  
    

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def letterScore (letter, scoreList):
    """ Returns numerical point value for given letter """
    
    if scoreList == []:
        return 0
    
    if letter == (scoreList[0])[0]:
        return(scoreList[0])[1]
    
    return letterScore (letter, scoreList[1:])


def explode(S):
    """ Takes string S and returns a list of the characters """
    
    sList = list(S)
    if sList == []:
        return []
    
    return list(S[0]) + explode(S[1:])


def wordScore (S, scoreList):
    """ Calculates scrabble score for string S,
        based on point values for each character of S """
    
    sList = explode(S)
    if (sList == []):
        return 0
    
    return letterScore(sList[0], scoreList) + wordScore(S[1:], scoreList)


def wordsWithScore(dct, scores):
    """ List of words in dct, with their Scrabble score """
    
    allWords = list(map(lambda S: [S, wordScore(S, scores)], dct))
    return allWords


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def take(n, L):
    """ Returns the list L[0:n], assuming L is a list and n is at least 0 """

    if n >= len(L):
        return L

    elif n == 0:
        return []

    return [L[0]] + take(n - 1, L[1:])



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def drop(n, L):
    """ Returns the list L[n:], assuming L is a list and n is at least 0 """

    if n >= len(L) or L == []:
        return []

    elif n == 0:
        return L

    return drop(n - 1, L[1:])


