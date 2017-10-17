class student(object):
    def __init__(self):
        pass
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self._score = score

    #直接访问
    @property
    def score(self):
        return self._score

    #等号调用该方法
    @score.setter
    def set_score(self, value):
        self._score = value

    #相当于toString
    def __str__(self):
        return self.name + ':' + str(self.age) + ':' + str(self._score)

s = student('adda',31,113)
print(s.score)
s.set_score = 20
print(s.score)
print(s)

#类用于for.....in
class fib(object):
    def __init__(self):
        self.a, self.b = 0,1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration
        return self.a

    #用于获取下标
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, b + a
            return a
        #sclice
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, b + a
            return L
    #对对象本身调用
    def __call__(self, *args, **kwargs):
        print(args,kwargs)

for n in fib():
    print(n)
print(fib()[5])
print(fib()[5:10])
f = fib()
#调用call
f(21,21,1,'dsad','sd212',kwargs = {'dad':213, 213:2131})
