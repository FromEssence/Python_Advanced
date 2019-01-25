def select(lst):
    tmax = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            for k in range(j+1, len(lst)):
                tri = sorted([lst[i], lst[j], lst[k]])
                if tri[0]+tri[1]>tri[2] and sum(tri)>tmax:
                    tmax = sum(tri)
    return tmax
lst = list(map(int, input().split()))
print (select(lst))

'''
#精致的数 x^i+y^j=n
def select(x,y,n):
    r = set()
    for i in range(n):
        for j in range(n):
            l = x**i+y**j
            if l <= n:
                r.add(l)
    return sorted(r)
x, y, n = int(input()), int(input()), int(input())
print(select(x,y,n))
'''

'''
#判断那两个数的和是给定值
def select(lst, s):
    for a in lst:
        for b in lst:
            if a != b and s == a+b:
                return sorted([lst.index(a), lst.index(b)])
lst = list(map(int, input().split()))
s = int(input())
print(select(lst, s))
'''

'''
#sort students by total score
class Student:
    def __init__(self, name, mscore, cscore, escore):
        self.sname = name
        self.mscore = mscore
        self.cscore = cscore
        self.escore = escore
    def __lt__(self, y):
        return self.tolScore()>y.tolScore()
    def __str__(self):
        return self.sname+' '+str(self.mscore)+' '+str(self.cscore)+' '+str(self.escore)
        #或：'%s %d %d %d' %(self.n, self.cscore, ...)
    def tolScore(self):
        return self.mscore+self.cscore+self.escore

sNames = input().split()
mscores = list(map(int, input().split()))
cscores = list(map(int, input().split()))
escores = list(map(int, input().split()))
# print(mscores)
lis = list()
for i in range(len(sNames)):
    lis.append(Student(sNames[i],mscores[i],cscores[i],escores[i]))
lis.sort()
print(lis[0])
'''
