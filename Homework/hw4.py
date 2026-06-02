def add_adjacent(previous, n):
    ''' Computes elements in row[1:-1] (i.e. middle of the row)'''
    
    if n <= 1:
        return []
    
    else:
        return [previous[0] + previous[1]] + add_adjacent(previous[1:], n - 1)
        

def pascal_row(n):
    ''' Outputs list of elements in nth row of Pascal's Triangle '''

    if n < 0:
        print('Invalid input')
        return
    
    elif n == 0:
        return [1]
    
    else:
        previous = pascal_row(n - 1)
        row = [1] + add_adjacent(previous, n) + [1]
        return row
        
        
def pascal_triangle(n):
    ''' Outputs list of rows up to nth row of Pascal's Triangle '''

    if n < 0:
        print('Invalid input')
        return
    
    elif n == 0:
        return [pascal_row(n)]

    else:
        return pascal_triangle(n-1) + [pascal_row(n)]


def test_pascal_row():
    ''' Compares output of pascal_row(n) to expected answer '''
    assert pascal_row(0) == [1]
    assert pascal_row(2) == [1, 2, 1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]
    assert pascal_row(7) == [1, 7, 21, 35, 35, 21, 7, 1]
    assert pascal_row(12) == [1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1]


def test_pascal_triangle():
    ''' Compares output of pascal_triangle(n) to expected triangle '''
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(7) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]]
