
# Extra credit (incorporating COMPRESSED_BLOCK_SIZE) was attempted.

from functools import reduce

# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1


def numToBinary(n):
    ''' Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n. '''
    if n == 0:
        return ''
    else:
        if n%2 != 0:
            s = '1'                 # Concatenate base-2 of int(n/2) with '1' if n is odd
        else:
            s = '0'                 # '0' if n is even
        return numToBinary(n // 2) + s


def binaryToNum(s):
    ''' Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s. '''
    if s == '':
        return 0
    else:
        if s[-1] == '1':
            return (binaryToNum(s[:-1]) * 2) + 1
        if s[-1] == '0':
            return (binaryToNum(s[:-1]) * 2)


def consecutive(s, binary, count):
    ''' Returns number of consecutive bits (as a base-10 integer) '''
    if s == '' or count >= MAX_RUN_LENGTH or not s[0] == binary:
        return count
    else:
        return consecutive(s[1:], binary, count + 1)


def constructRLS(s, binary):
    ''' Creates run-length sequence as a list '''
    
    if s == '':
        return []
    
    count = consecutive(s, binary, 0)

    if binary == '0':
        next_call = '1'
    else:
        next_call = '0'
    return [count] + constructRLS(s[count:], next_call)


def bits(s):
    ''' Ensures all blocks are five bits such that each block represents a base-2 number '''
    if len(s) < COMPRESSED_BLOCK_SIZE:
        return ((COMPRESSED_BLOCK_SIZE - len(s)) * '0') + s
    return s


def compress(s):
    ''' Returns run-length encoding of an image, expressed as a binary string '''
    binaryRLS = list(map(lambda x: bits(numToBinary(x)), constructRLS(s, '0')))
    return reduce(lambda x, y: x + y, binaryRLS)


'''
Explain what is the largest number of bits that your compress algorithm could 
possibly use to encode a 64-bit string/image.

Largest number of bits that compress can output for 64-bit image: (64 * COMPRESSED_BLOCK_SIZE)
Worst case scenario means there are no consecutive pixels, which means every block will alternate
between '00000' or '00001'. This means 5 bits, copied 64 times.
'''


def compressedToRLS(s):
    ''' Precondition: input is a binary string representing a compressed image.
    Returns a list of the run-length sequence as base-10 integers. '''
    if s == '':
        return []
    else:
        return [binaryToNum(s[:COMPRESSED_BLOCK_SIZE])] + compressedToRLS(s[COMPRESSED_BLOCK_SIZE:])


def uncompress(s):
    ''' Reverses the run-length encoding of an image, expressed as a binary string '''
    def deconstructRLS(L, binary):
        if L == []:
            return ''
        if binary == '0':
            seq = '0' * L[0]
            next_call = '1'
        else:
            seq = '1' * L[0]
            next_call = '0'
        return seq + deconstructRLS(L[1:], next_call)
    return deconstructRLS(compressedToRLS(s), '0')


def compression(s):
    ''' Returns the ratio of the compressed and original sizes for image s '''
    return len(compress(s)) / len(s)


def test():
    ''' Tests compression ratios for images '''
    print("White Block: " + str(compression("0" * 64)))
    print("Stripes: " + str(compression("1" * 16 + "0" * 16 + "1" * 16 + "0" * 16)))
    print("Diagonal: " + str(compression("0" * 15 + "1" + "00000011" + "00000111" + "00001111" + "00011111" + "00111111" + "0" + "1" * 15)))
    print ("Penguin: " + str(compression("00011000" + "00111100"*3 + "01111110" + "11111111" + "00111100" + "00100100")))
    print("Smile: " + str(compression("0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8)))
    print("Five: " + str(compression("1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0")))


'''
EXPLANATION FOR COMPRESSION TEST IMAGES

For our test images, we tested a fully white block and an image with four alternating stripes.
Their compression ratios are the same because though the white block contains more consecutive
pixels, the block size limits the run length we can encode. Their compression ratios were
significantly less than 1, demonstrating that the compressed string is shorter than the original.

Our next image repesents a diagonal across the image, where one side is white and the other black.
Its compression ratio was 0.9, which also indicates that the compressed string is successful in
condensing the image.

However, for the last 3 images, their compression ratios are greater than 1
(indicating that the compressed string is longer), likely because they are more complex and thus
contain less consecutive pixels.
'''

'''
EXPLANATION FOR LAI'S COMPRESS
Professor Lai cannot guarantee that the compression algorithm will always return a shorter
string because the length depends on the frequency of consecutive pixels. Worst case scenario,
a 64-pixel image without any consecutive pixels must output 64 repeats of '00001' (or however
long the block is, as set by COMPRESSED_BLOCK_SIZE). Since there are "unnecessary" 0's needed
to represent just "1", the compression will inevitably lengthen rather than shorten the string.
'''
