#如果c是C的实例化,c.x 将触发getSize,c.x = value将触发setSize,size将赋值为1,即c.size=1,del c.x 触发 delSize,使size的值删除
class C:
    def __init__(self, size = 10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self, value):
        self.size = value
    def delSize(self):
        del self.size
    x = property(getSize, setSize, delSize)

c = C()
c.x = 1
c.size = 1
del c.x