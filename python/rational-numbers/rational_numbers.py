from __future__ import division

def gcb(x,y):
    #返回两个数的最大公约数
    if y>x:
        tmp = x
        x=y
        y=tmp
    if y == 0:
        return x
    remainder = x%y
    while remainder!=0:
        x=y
        y=remainder
        remainder = x%y
    return y
    

class Rational(object):
    def __init__(self, numer, denom):
        if denom == 0:
            raise ValueError("denominator cannot be 0")
        if not (isinstance(numer,int) and isinstance(denom,int)):
            raise ValueError("numerator and denominator should both be integers") 
        div = gcb(numer,denom)
        self.numer = numer//div
        self.denom = denom//div

    def __eq__(self, other):
        return ((self.numer == other.numer and self.denom == other.denom) or
                (self.numer == -other.numer and self.denom == -other.denom))

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = self.numer*other.denom+self.denom*other.numer
        denom = self.denom*other.denom
        return Rational(numer,denom)

    def __sub__(self, other):
        numer = self.numer*other.denom-other.numer*self.denom
        denom = self.denom*other.denom
        return Rational(numer, denom)

    def __mul__(self, other):
        return Rational(self.numer*other.numer,self.denom*other.denom)

    def __truediv__(self, other):
        return Rational(self.numer*other.denom,self.denom*other.numer)

    def __abs__(self):
        return Rational(abs(self.numer),abs(self.denom))

    def __pow__(self, power):
        if power >= 0:
            return Rational(self.numer**power,self.denom**power)
        else:
            return Rational(self.denom**power,self.numer**power)

    def __rpow__(self, base):
        return pow(base**self.numer,1/self.denom)
