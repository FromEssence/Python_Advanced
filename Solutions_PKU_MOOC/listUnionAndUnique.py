'''#输入两个列表alist和blist，要求列表中的每个元素都为正整数且不超过10；
#合并alist和blist，并将重复的元素去掉后输出一个新的列表clist。
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

clist = alist+blist #union

set_s = set(clist) #unique
uniLis = list(set_s)
print(sorted(uniLis))
'''
'''
alist = list(map(int, input().split()))
mid = len(alist)//2
fist_half = alist[:mid]
seco_half = alist[mid:]

dict_d = dict()
dict_d['1'] = fist_half
dict_d['2'] = seco_half

print(dict_d)
'''

#反转列表
alist = list(map(int, input().split()))
rev_ali = list(reversed(alist))

print(rev_ali)
