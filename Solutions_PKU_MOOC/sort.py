#列表自定义排序
#python3传递的排序函数返回的是代表自身相对位置的数值
def cmp(x):
    return abs(x)

alist=list(map(int,input().split()))
b = sorted(alist, key=cmp)
print(b)
