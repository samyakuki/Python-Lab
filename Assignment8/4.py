class Shape:
    def __init__(self, length):
        self.length = length

    def get_area(self):
        print("Area is 0")  
class Square(Shape):  
    def __init__(self, length):
        super().__init__(length)  

    def get_area(self):
        
        print(f"Area of square is {(self.length) * (self.length)}") 

shape = Shape(5)
shape.get_area() 

square = Square(4)
square.get_area()  
