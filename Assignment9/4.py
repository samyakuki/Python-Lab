class Base1:
    def process(self):
        print("Base1")

class Base2:
    def process(self):
        print("Base2")

class Base3:
    def process(self):
        print("Base3")

class Derived(Base1, Base2, Base3):
    def process(self):
        super().process()

d = Derived()
d.process()

Derived.__bases__ = (Base2, Base1, Base3)  

d = Derived()
d.process()

Derived.__bases__ = (Base3, Base2, Base1)  

d = Derived()
d.process()
