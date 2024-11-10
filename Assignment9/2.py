class A():
    def action(self):
        print("This is a method from class A")

class B(A):
    def action(self):
          super().action()
          print("This is a method from class B")

class C(A):
    def action(self):
        super().action()
        print("This is a method from class C")

class E(A):
    def action(self):
        super().action()
        print("This is a method from class E")


class D(B,C,E):
    def action(self):
        super().action()
        print("This is a method from class D")


d = D()



d.action()

