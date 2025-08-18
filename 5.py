class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        self.area=2*3.14*self.radius**2
        return self.area
    def perimeter(self):
        self.peri=2*3.14*self.radius
        return self.peri
c1=circle(2)
print(c1.area())
print(c1.perimeter())