class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.__marks = None
        self.setmarks(marks)
    def setmarks(self,marks):
        if(marks>=0 and marks<=100):
            self.__marks=marks
        else:
            print("Invalid input")
    def getmarks(self):
        print(f"Student marks are: {self.__marks}")
std = Student('XYZ',179,86)
print(std.getmarks())
std.setmarks(90)
print(std.getmarks())
