
import math
class QuadraticEquation(object):

    def __init__(self, a, b, c):
        '''  Constructor for QuadraticEquation '''
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def getA(self):
        ''' Takes a as an argument '''
        return self.a
    
    def getB(self):
        ''' Takes c as an argument '''
        return self.b
    
    def getC(self):
        ''' Takes c as an argument '''
        return self.c

    def discriminant(self):
        ''' Returns the discriminant (b^2-4ac) '''
        a = self.getA()
        b = self.getB()
        c = self.getC()
        return b**2 - 4*a*c

    def root1(self):
        ''' Returns positive root of quadratic equation '''
        a = self.getA()
        b = self.getB()
        c = self.getC()
        disc = self.discriminant()
        if disc < 0:
            return None
        return (-b + math.sqrt(disc))/(2*a)

    def root2(self):
        ''' Returns negative root of quadratic equation '''
        a = self.getA()
        b = self.getB()
        c = self.getC()
        disc = self.discriminant()
        if disc < 0:
            return None
        return (-b - math.sqrt(disc))/(2*a)

    def __str__(self):
        ''' Returns string representation of quadratic equation '''
        if self.a < 0:
            a_sign = '-'
        else:
            a_sign = ""
        if self.b < 0 or self.c < 0:
            b_sign = '-'
        else:
            b_sign = '+'
        if self.c < 0:
            c_sign = '-'
        else:
            c_sign = '+'
        if self.a == 1 or self.a == -1:
            a = ''
        else:
            a = str(abs(self.a))
        if self.b == 0:
            b = ''
        elif self.b == 1 or self.b == -1:
            b = b_sign + ' x '
        else:
            b = b_sign + ' ' + str(abs(self.b)) + 'x '
        if self.c == 0:
            c = ''
        else:
            c = c_sign + ' ' + str(abs(self.c)) + ' '
        return a_sign + a + 'x^2 ' + b + c + '= 0'
    
