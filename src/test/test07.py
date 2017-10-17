import types

def add(self, x):
    self.x = x + 10

class student(object):
    def __init__(self):
        pass
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.__score = score

    def score(self):
        print(self.name, self.age)
        return

#动态添加
s = student("jinek", 12, 1)
s.aa = 'aa'
s.fun = types.MethodType(add, s)

print(s.fun(21))
print(student("sad", 21, 21).age)

print(type(student("dsa",2,1).score) == types.MethodType)

#限制动态添加__slots__变量
class st(object):
    __slots__ = ('name', 'age')

k = st()
k.name = 10
