class Rectangle:
    def __init__(self, length,width):
        self.length=length
        self.width=width

    def get_area(self):
        print(f"Area is {(self.length)*(self.width)}")


a=Rectangle(5,7)
a.get_area()
