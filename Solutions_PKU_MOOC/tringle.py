triange = [1]
print(triange)

triange.append(0)
n=10
for i in range(1,n):
    newline = []
    for j in range(i+1):
        value = triange[j]+triange[-j-1]
        newline.append(value)

    print(newline)
    triange = newline

    triange.append(0)
