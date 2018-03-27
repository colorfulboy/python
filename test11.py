# 用filter（）取回数
def is_palindrome(n):
    s=str(n)
    return s==s[::-1]
output=filter(is_palindrome,range(1,1000))
print(list(output))


# 用sorted给姓名和成绩排序：
L=[('Bob',75),('Adam',92),('Brt',66),('Lisa',88)]
def by_name(t):
    return t[0].lower()
L1=sorted(L,key=by_name)
print(L1)
def by_score(t):
    return t[1]
L2=sorted(L,key=by_score,reverse=True)
print(L2)