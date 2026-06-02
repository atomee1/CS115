

import sys
import importlib

# Fibonacci
# HMMM functino that accepts integer n and prints first n Fibonacci numbers

Fibonacci = '''
00    read    r1            # read n
01    setn    r2 1          # set r2 = 1
02    sub     r3 r1 r2      # set r3 = r1 - 1
03    jltzn  r3 15         # halt if n < 1
04    setn    r4 1          # set a = 1
05    setn    r5 0          # set b = 0
06    setn    r6 1          # set k = 1
07    add     r7 r4 r5      # set c = a + b
08    write   r5            # print b
09    addn    r6 1          # k += 1
10    copy    r5 r4         # b = a
11    copy    r4 r7         # a = c
12    sub     r8 r6 r1      # r8 = k - n
13    jgtzn   r8 15         # halt if k > n
14    jumpn   07            # loop back to 07
15    halt
'''

# Set this variable to whichever program you want to execute
# when this file is loaded.
RunThis = Fibonacci

# Choose whether to use debug mode; uncomment one of the following lines.
# Mode = ['-n'] # not debug mode, 
Mode = ['-d'] # debug mode
#Mode = []     # prompt for whether to enter debug mode


# When you press F5 in IDLE, the following code will
# load the assembler and simulator, then run them.
# You can interrupt with Ctrl-C; then re-start Python.

if __name__ == "__main__" : 
    import hmmmAssembler ; importlib.reload(hmmmAssembler)
    import hmmmSimulator ; importlib.reload(hmmmSimulator)
    hmmmAssembler.main(RunThis) # assemble input into machine code file out.b
    hmmmSimulator.main(Mode)    # run the machine code in out.b

