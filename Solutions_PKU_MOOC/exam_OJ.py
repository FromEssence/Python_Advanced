'''#1
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
ans = 0
for i in range(len(alist)):
    ans += (alist[i]-blist[i])**2
print(ans)
'''
'''#2
s = str(input())
#s.replace(' ', '')
#s = ''.join(s.split())
ss=""
for i in range(len(s)):
    if s[i].isdigit() or s[i].isalpha():
        ss += s[i]
ss = ss.lower()
#print(ss)
flag = True
for i in range(len(ss) // 2):
    if ss[i]!=ss[-1-i]:
        flag = False
        break
if len(ss)==0:
    print(False)
else:
    print(flag)
'''

'''#3
alist = list(map(str, input().split()))
alist.sort()
st = set()
ans = 0
for i in range(len(alist)-2):
    for j in range(i+1, len(alist)):
        for k in range(j+1, len(alist)):
            if int(alist[i])+int(alist[j])+int(alist[k])==0:
                tmp = alist[i]+alist[j]+alist[k]
                st.add(tmp)
                
print(len(st))    
'''

'''#4
alist = list(map(int, input().split()))
s = 1
cnt_0=0 #number of 0
for a in alist:
    if a != 0:
        s *= a
    else:
        cnt_0 += 1
for i in range(len(alist)):
    if alist[i]==0:
        if cnt_0>1:
            alist[i]=0
        else:
            alist[i] = s
    else:
        if cnt_0>0:
            alist[i]=0
        else:
            alist[i] = int(s / alist[i])
print(alist)
'''
#5

#按密钥解密
def decode(cip, key):
    plain = ""
    for i in range(len(cip)):
        plain += chr( ord('A')+(ord(cip[i])-ord('A')+key)%26)
    return plain
#判断是不是以BYE结尾
def judge(s):
    #tmp = str(s[-3:])
    return s[-3:] == "BYE"

cipher = str(input())
for i in range(26):
    #print(decode(cipher, i))
    if judge(decode(cipher, i)):
        print(decode(cipher, i))
        break 