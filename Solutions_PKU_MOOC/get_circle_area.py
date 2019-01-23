
'''求圆面积和周长
pi=3.14159

r = int(input())
print(round(2*pi*r, 4),end=" ")
print(round(r*r*pi, 4))
'''

'''求给定合法三角形的面积
import math
a = int(input())
b = int(input())
c = int(input())

p = (a+b+c)/2

print('%.2f' %(math.sqrt(p*(p-a)*(p-b)*(p-c))))

'''

'''计算字符在字符串中出现次数
s = str(input())
strs = s.split()

ori = strs[0]
pattan = strs[1]
cnt=0
for i in range (len(ori)):
    if(pattan==ori[i]):
        cnt += 1

print(cnt)
'''
s = str(input())
strs = s.split()
print(len(strs[-1]))
