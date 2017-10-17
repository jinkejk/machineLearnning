from functools import partial

z = 10
def out(x, y):
    def sum():
        return x + y + z
    return sum

f = out(3, 4)
print(f())

#函数的闭包，函数内会检测ｚ的变化
z = 20
print(f())

#偏函数
def foo(a,b,c):
    return a+b+c

foo2 = partial(foo, b=2)
print(foo2(a=1, c=3))

bin2dec = partial(int, base=2) #二进制
hex2dec = partial(int, base=16) #16进制

int('15') #=>15  using default base 10
print(bin2dec('01011'))
print(hex2dec('67'))
print(int('67', base=8))

def _private(x):
    return x

