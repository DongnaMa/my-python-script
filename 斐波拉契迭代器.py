#for … in… 这个语句其实做了两件事.第一件事是获得一个可迭代器,即调用了__iter__()函数,第二件事是循环的过程，循环调用__next__()函数.

class Fibs:
    def __init__(self, n=10):
        self.a = 0
        self.b = 1
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a +self.b
        if self.a > self.n:
            raise StopAsyncIteration
        return  self.a

fibs = Fibs()
for each in fibs:
    print(each)
