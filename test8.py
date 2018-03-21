#-*- coding: utf-8 -*
'''L=[]
n=1
while n<=99:
    L.append(n)
    n=n+2
    print(L)
#切片
L=list(range(100))
print(L[0:11:5])'''
#矢代
#判断是矢代还是矢代器
from collections import Iterable ,Iterator

def g():

    yield 1
    yield 2
    yield 3

print('Iterable? [1,2,3]:',isinstance([1,2,3],Iterable ) )
print('Iterable? \'abc\':',isinstance('abc',Iterable ))
print('Iterable? 123:',isinstance(123,Iterable ))
print('Iterable? g():',isinstance(g(),Iterable ))

print('Iterator? [1,2,3]:',isinstance([1,2,3],Iterator ))
print('Iterator? iter(1,2,3):',isinstance(iter([1,2,3]),Iterator ))
print('Iterator? \'abc\':',isinstance('abc',Iterator ))
print('Iterator? 123:',isinstance(123,Iterator ))
print('Iterator? g():',isinstance(g(),Iterator ))

#  iter list
print('for x in [1,2,3,4,5]:')
for x in [1,2,3,4,5]:
    print(x)


print('for x in iter([1,2,3,4,5]):')
for x in iter([1,2,3,4,5]):
    print(x)

print('next():')
it =iter([1,2,3,4,5])
print(next(it ) )
print(next(it ) )
print(next(it ) )
print(next(it ) )
print(next(it ) )

d={'a':1,'b':2,'c':3}

# iter each key
print('iter key:',d )
for k in d.keys():
    print('key:',k)

# iter each value
print('iter value:',d)
for v in d.values() :
    print('value:',v)

# iter both key and value
print('iter item:',d)
for k ,v in d.items():
    print('item:',k,v)

# iter list with index
print('iter enumerate([\'A\',\'B\',\'C\'])')
for i ,value in enumerate(['A','B','C']):
    print(i,value)

# iter complex list
print('iter[(1,1),(2,4),(3,9)]:')
for x,y in[(1,1),(2,4),(3,9)]:
    print(x,y)




# 列表生成器，请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L1=['Hello','World',18,'Apple',None]
L2=[s.lower() for s in L1 if isinstance(s,str) ]
print(L2)