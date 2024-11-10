class X:
    def greet(self):
        print("Hello from X")

class Y:
    def greet(self):
        print("Hello from Y")

class Z(X, Y):
    def greet(self):
        super().greet()

z = Z()
z.greet()

print(Z.mro())  