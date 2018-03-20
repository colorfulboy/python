# -*- coding: utf-8 -*-
import math
a=int(input('input a:') )
b=int(input('input b:') )
c=int(input('input c:') )
def quadirtic(a,b,c):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float) ):
        raise TypeError ('bad operand type')

    s=b*b -4*a*c
    if s>0:
        x1=(-b+math.sqrt(s))/(2*a)
        x2=(-b-math.sqrt(s))/(2*a)
        return x1,x2
    elif s==0:
        x=(-b)/(2*a)
        return x
    else:
        return'无解'
print(quadirtic(a,b,c) )




