
from cs5png import *


def mult(c,n):
    ''' Uses only a loop and addition to multiply c by n '''
    result = 0
    for x in range(n):
        result += c
    return result


def update(c,n):
    ''' Starts with z = 0 and runs z = z**2 + c for n times '''
    z = 0
    for x in range(n):
        z = z**2 + c
    return z


def inMSet(c,n):
    ''' Return True if complex number c is in Mandelbrot set
        Takes in
            c for the update step of z = z**2 + c
            n, the maximum nymber of times to run that step
        Then, it should return
            False as soon as abs(z) gets larger than 2
            True if abs(z) never gets larger than 2 (for n iterations) '''
    z = 0
    for x in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True
    

def weWantThisPixel(col,row):
    ''' Returns True if we want pixel at col, row. False otherwise '''
    if col%10 == 0 or row%10 == 0:
        return True
    else:
        return False


def test():
    ''' Function to demonstrate how to create and save png image '''
    width = 300
    height = 200
    image = PNGImage(width,height)

    # Create a loop in order to draw pixels

    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col,row) == True:
                image.plotPoint(col,row)

    # Write the file after looping through every image pixel

    image.saveFile()

# Changing "and" to "or" in "if col%10 == 0 and row%10 == 0" will fill in all pixels
# in the specified row or column, creating a full grid instead of a dotted grid.


def scale(pix, pixMax, floatMin, floatMax):
    ''' scale takes in
            pix, the CURRENT pixel column (or row)
            pixMax, the total # of pixel columns
            floatMin, the min floating-point value
            floatMax, the max floating-point value
        scale returns the floating-point value that corresponds to pix '''
    ratio = (1.0 * pix) / pixMax
    difference = floatMax - floatMin
    result = (ratio * difference) + floatMin
    return result


def mset():
    ''' Creates 300x200 image of Mandelbrot set '''
    width = 300
    height = 200
    image = PNGImage(width,height)

    # Create a loop in order to draw pixels

    for col in range(width):
        for row in range(height):
            # Create complex number c
            x = scale(col,300,-2.0,1.0)
            y = scale(row,200,-1.0,1.0)
            c = x + y*1j
            if inMSet(c,25) == True:
                image.plotPoint(col,row)

    # Write the file after looping through every image pixel

    image.saveFile()
