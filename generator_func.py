#生成器函数
def even_number(max):
    n=0
    while n < max:
        yield n
        n += 2
for i in even_number(10):
    print(i)
