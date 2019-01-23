days = int(input())
cnt=1
for i in range(days-1):
    cnt = (cnt+1)*2
print(cnt)

'''#素数
import math
def judge(x):
    t = int(math.sqrt(x))
    for i in range(2, t+1):
        if x % i == 0:
            return False
    return True
n = int(input())
res = []
for i in range(2,n):
    if(judge(i)):
        res.append(i)
print(sorted(res))
'''

'''#金字塔
n = int(input())
length = int(2*n-1)
for i in range(1,n+1):
    
    for j in range(n-i):
        print(' ', end='')
    for j in range(int(i*2)-1):
        print('+', end='')
    print('')
    #for j in range(i,n):
       # print(' ')
'''

'''#求出完数
def judge_complet_num(n):
    cnt=0
    length = len(str(n))
    for i in range(1,n):
        if n % i ==0:
            cnt += i
    if cnt==n:
        return True
    return False

max = int(input())

for i in range(1,max+1):
    if(judge_complet_num(i)):
        print(i)
'''

'''#回文串判断
n = str(input())
flag = 0
for i in range(len(n) // 2):
    if n[i] != n[len(n)-1-i]:
        print('no')
        flag = 1;
        break
if(flag==0):
    print('yes')
'''

'''#与7有关的数
def is7Related(x):
    if(x % 7 == 0):
        return True
    while x>0:
        if(x%10 == 7):
            return True
        x //= 10
    return False
max = int(input())

tol = 0
for i in range(1,max+1):
    if(is7Related(i) == False):
        tol += i**2
print(tol)
'''

'''#字符集合合并
s1 = str(input())
s2 = str(input())
set_s = set()

for s in s1:
    set_s.add(s)
for s in s2:
    set_s.add(s)
print(sorted(set_s)) #返回列表
'''

'''#水仙花数
def judge_flower_num(n):
    cnt=0
    length = len(str(n))
    tmp = n
    while tmp>0:
        cnt += (tmp%10)**length
        tmp = tmp // 10
    if cnt==n:
        return True
    return False

max = int(input())

for i in range(100,max+1):
    if(judge_flower_num(i)):
        print(i)
'''
