#################################################################
# Name: Katie Ng
# Date: 09 February 2022
# Pledge: I pledge my Honor that I have abided by the Stevens Honor Code.

# CS115 Homework 2
# File Name: hw2.py
#################################################################


import sys
sys.setrecursionlimit(10000) # Allows up to 10000 recursive calls


from functools import reduce
#from dict import *
#from bigdict import *

""" Global list of Scrabble letters and their respective point values """
scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1],
["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1],
["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], ["s", 1],
["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]

Dictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo",
"spam", "spammy", "zzyzva"]



def letterScore (letter, scoreList):
    """ Returns numerical point value for given letter """
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


def scoreList(rack):
    """ Given list of letters, return list of all possible words in global dictionary """
    possibleWords = []
    for word in Dictionary:
        isPossible = True
        for char in word:
            if char not in rack:
                isPossible = False
                continue
        if isPossible:
            possibleWords.append([word, wordScore(word, )])
    return possibleWords

def comparePairs(x, y):
    if x[1] > y[1]:
        return x
    return y

def bestWord(rack):
    possibleWords = scoreList(rack)
    if possibleWords == []:
        return ["", 0]
    return reduce(comparePairs, possibleWords)





