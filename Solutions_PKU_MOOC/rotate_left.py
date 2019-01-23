s = str(input())
n = int(input())

d = dict()

for i in range(len(s)):
    tmp = (i-n+len(s)) % len(s)
    d[tmp] = s[i]

for i in range(len(s)):
    print(d[i],end="")
