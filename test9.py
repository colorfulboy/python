#-*- coding: utf-8 -*
# map/reduce:

#转首字母大写：
def normalize(name):
    return name.capitalize()
L1=['adam','LISA','barT']
L2=list(map(normalize,L1 ) )
print(L2)


#编写prod（）函数，接受一个list并利用reduce（）函数求积：
from functools import reduce
def prod(L):
    def product_rule(x,y):
        return x*y
    return reduce(product_rule,L )
print('3*5*7*9=',prod([3,5,7,9]) )

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce
def str2float(s):
    def fn(x,y):
        return 10*x+y
    n=s.index('.')
    s1=list(map(int,[x for x in s[:n]]) )
    s2=list(map(int,[x for x in s[n+1:]]) )
    return reduce(fn,s1 )+reduce(fn,s2)/10**len(s2)
print('\'123.4567\'=',str2float('123.4567'))
