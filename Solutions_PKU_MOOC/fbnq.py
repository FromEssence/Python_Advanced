#bubble sort
def bubbleSort(lis):
    for i in range(len(lis)):
        for j in range(len(lis)-i-1):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
    return lis

alist=list(map(int,input().split()))
print(bubbleSort(alist))

'''#得到列表奇数位置元素
def foo(lis):
    return lis[1::2]

alist=list(map(int,input().split()))
print(foo(alist))
'''

'''#gcd & lcm
def hcf(x, y): 
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd
def lcm(a, b):
    return int(a*b/hcf(a, b))
num1=int(input(""))
num2=int(input(""))
print(lcm(num1,num2))
'''

'''#gcd
import math
def hcf(a, b):
    return math.gcd(a, b)
num1=int(input(""))
num2=int(input(""))
print(hcf(num1,num2))
'''

'''#fbnq
def fbnq(n):
    if n==1 or n==2:
        return 1
    a1=1
    a2=1
    res=0
    for i in range(2,n):
        res = a1+a2
        a1=a2
        a2=res
    return res
    

n = int(input())
print(fbnq(n))
'''

