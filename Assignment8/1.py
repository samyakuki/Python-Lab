class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        print(f"Area is {3.14 * (self.radius)**2}")

c = Circle(5)
c.get_area()
