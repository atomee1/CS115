
import random
import sys


def createOneRow(width):
    """ Returns one row of zeros of width "width"...  """
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width,height):
    """ Returns 2D array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

def printBoard(A):
    """ Prints 2D list-of-lists A without spaces
        (using sys.stdout.write) """
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')
        
def diagonalize(width,height): 
    """ Creates an empty board and then modifies it 
        so that it has a diagonal strip of "on" cells. """ 
    A = createBoard( width, height ) 
    for row in range(height): 
        for col in range(width): 
            if row == col: 
                A[row][col] = 1 
            else: 
                A[row][col] = 0      

    return A

def innerCells(width, height):
    """ Returns 2D array of all live cells except
        for a one-cell-wide border of empty cells
        (with the value of 0) around the edge of 2D array. """
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height - 1 or col == 0 or col == width - 1:
                A[row][col] = 0
            else:
                A[row][col] = 1     
    return A

def randomCells(width,height):
    """ Returns array of randomly-assigned 1's and 0's 
        except that the outer edge of the array is empty """
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height - 1 or col == 0 or col == width - 1:
                A[row][col] = 0
            else:
                A[row][col] = random.choice([0,1])     
    return A

def copy(A):
    """ Returns a deep copy of the 2D array A. """
    newCopy = createBoard(len(A[0]), len (A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            newCopy[row][col] =  A[row][col]
    return newCopy

def innerReverse(A):
    """ Returns 2D array with reversed inner cells"""
    newCopy = innerCells(len(A[0]), len(A))
    for row in range(1, len(A) - 1):
        for col in range(1, len(A[0]) - 1):
            if A[row][col] == 1:
                newCopy[row][col] = 0
            else:
                newCopy[row][col] = 1
    return newCopy

def next_life_generation(A):
    """ Makes a copy of A and then advanced one generation of Conway's game of
    life within the *inner cells* of that copy. Outer edge stays 0. """
    newA = copy(A)
    for row in range(1, len(A) - 1):
        for col in range(1, len(A[0]) - 1):
            curV = A[row][col]
            neighbors = countNeighbors(row, col, A) 
            if curV == 1 and neighbors < 2 or neighbors > 3:
                newA[row][col] = 0
            elif curV == 0 and neighbors == 3:
                newA[row][col] = 1
    return newA

def countNeighbors(row, col, A):
    """ Returns the number of live neighbors for a
        cell in the board A at a particular row and col. """
    return sum([A[row-1][col], A[row-1][col+1], A[row][col+1], A[row+1][col+1], A[row+1][col],
        A[row+1][col-1], A[row][col-1], A[row-1][col-1]])



