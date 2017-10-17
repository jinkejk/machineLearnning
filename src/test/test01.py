import math

#default parameter
from collections import Iterable

import os


def fun01(x, y = 3):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError('type error!')
    else:
        z = math.pow(x, 2) + math.pow(y, 2)
        return x + y, x, y, z

#默认参数,最好使用不可变量
def fun02(l = []):
    l.append('len')
    return l

print(fun02())
print(fun02())
print(fun02())
print(fun02())
print(fun02())
print(fun01(4))

#命名关键字参数
#可变参数后面参数,调用要加参数名
def fun03(a, *b, c):
    return 'ada'
print(fun03('da',21,21,21, c=21))

print('adad',isinstance("sad", Iterable))

#获取下标
for i,v in enumerate([21,21,21,21,21]):
    print(i, v)

for x, y in [(21,2), (121,21)]:
    print(x, y)

print([x + y for x in 'asb' for y in 'klm'])

#列出当前目录下的文件
print(os.listdir('.'))

#
d = {"a":1, "b":2, "c":3}
print([x + '=' + str(y) for x, y in d.items()])

for i,v in enumerate('sadasdad'):
    print(i, v)

line = list([12,21,21,21,21])
line.append(211)
print(line)