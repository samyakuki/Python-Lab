class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.__salary=None
        self.setsalary(salary)
    def setsalary(self,salary):
        if(salary>=0):
            self.__salary=salary
        else:
            print("Invalid value")
    def getsalary(self):
        return self.__salary
emp = Employee('SVP',20,120000)
print(emp.setsalary(150000))
print(emp.getsalary())
