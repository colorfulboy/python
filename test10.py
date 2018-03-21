#-*- coding: utf-8 -*
# 智障小游戏：
from random import randint
num=randint(1,100)
print('你猜这个数字是啥？')
bingo=False
while bingo ==False:
    answer=int(input())
    if answer<num:
        print('%d太小了'%answer)
    if answer>num:
        print('%d太大了'%answer)
    if answer==num:
        print('%d是对的'%answer)
        bingo=True




# 函数：
def isEqua(num1,num2):
    if num1<num2:
        print('too samll')
        return False;
    if num1>num2:
        print('too  big')
        return False;
    if num1==num2:
        print('bingo')
        return True

from random import randint
num=randint(1,100)
print('Guess what i think?')
bingo=False
while bingo==False:
    answer=int(input())
    bingo=isEqua(answer,num )