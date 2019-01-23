#约瑟夫环
n = int(input())
m = int(input())
lst = list(range(n))
res = []
for i in range(n):
    for j in range(m-1):
        lst.append(lst.pop(0))
    res.append(lst.pop(0))
print(res)

'''#图案打印
n = int(input())-1
lst = ['X']*(2*n+1)
for i in range(n):
    s = '+'*i + 'X' + '+'*(n-i-1)
    s = s+'+'+s[::-1]
    lst[i] = lst[-1-i] = s
lst[n] = '+'*n+'X'+'+'*n
for l in lst:
    print(l)
'''

'''#平方数判别
def isSquare(x):
    if int(x**0.5) * int(x**0.5) == x:
        return True
    return False
    
i = 1
while True:
    if isSquare(i+150) and isSquare(i+286):
        print(i)
        break
    i += 1
'''


'''# 数学公式计算
from math import *
x = int(input())
ans = sin(15*pi/180) + (exp(x)-5*x)/sqrt(x*x+1) - log(3*x,e) #log底默认是e
print(round(ans, 10))
'''

'''
#第几天
import datetime

date_now = input()
d_list = date_now.split('/')
y = d_list[0]
m = d_list[1]
d = d_list[2]

inter_days = (datetime.datetime(int(y), int(m), int(d))-datetime.datetime(int(y), 1, 1)).days+1
print(inter_days)

'''
'''#第几天 更加python
from datetime import *
d = input()
d1 = datetime.strptime(d[:4]+'/1/1', '%Y/%m/%d')
d2 = datetime.strptime(d, '%Y/%m/%d')
print((d2-d1).days+1)
'''
