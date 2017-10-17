l = (1, 2, 3, 2, 31, 31)  # 不是generate是tuple
k = (x * x for x in range(10))
print(type(l))
print(type(k))  # gengerate 不断推算,并不会立即创建

for j in k:
    print(j)


def geti(n, i):
    if 0 <= i < len(n): return n[i]
    else: return 0

# 生成器
def triangles():
    l = [1]
    k = [1,1]
    while True:
        if len(l) == 1:
            l.append(1)
            yield '[1]'
        else:
            st = '['
            for i in range(len(l)):
                k[i] = (l[i] + geti(l, i -1))
                st = st + str(k[i]) + ','
            k.append(1)
            l = k
            st = st + '1]'
            yield st

    return 'done'


n = 0
for t in triangles():
    print(t)
    n += 1
    if n == 40:
        break
