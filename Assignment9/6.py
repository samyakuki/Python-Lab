
class Base1:
    def __init__(self):
        self.data="Base1 data"
    def info(self):
        print("Base1 info")
class Base2:
    def __init__(self):
        self.data = "Base2 data"
    def info(self):
        print("Base2 info")
class Base3:
    def __init__(self):
        self.data="Base3 data"
    def info(self):
        print("Base3 info")
class Combined(Base1,Base2,Base3):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        Base3.__init__(self)
    def info(self):
        return super().info()
c = Combined()
print(c.info())
print(c.data)
