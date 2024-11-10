class Person:
    def __init__(self,n,**kwargs):
        self.n = n
        super().__init__(**kwargs)
class Employee(Person):
    def __init__(self,n,salary,**kwargs):
        self.salary=salary
        super().__init__(n=n,**kwargs)
class Manager(Person):
    def __init__(self,n,department,**kwargs):
        self.department=department
        super().__init__(n=n,**kwargs)
class Director(Employee,Manager):
    def __init__(self, n, salary, department):
        super().__init__(n=n, salary=salary, department=department)
d = Director('Samya',4000000,'IT')
print(f"{d.n} works in {d.department} and has a salary of {d.salary} ")
