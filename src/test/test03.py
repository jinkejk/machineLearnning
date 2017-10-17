from functools import reduce

a = [1,2,3,4,5,6,7,8,9,10]

def fun01(x):
    x += 10;
    return x

def fun02(x, y):
    return x + y

b = map(fun01, a)
c = reduce(fun02, a)

print(c)

def fun03(x):
    return x[1]

d = [1,-2,21,3,-31,-45,-66]
dic = {"sas":12, "ad":13, "sd":14}

print(sorted(dic, key=lambda s: s[1], reverse=True))