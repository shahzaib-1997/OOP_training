class Circle():
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius


    def area(self):
        return Circle.pi*(self.radius**2)


    def set_radius(self, new_radius):
        self.radius = new_radius
        return 'Radius changed.'
    
    def get_radius(self):
        return self.radius
        
x = Circle(3)

Area = x.area()

print(f'Area of circle with radius {x.radius} is {Area}.')

status = x.set_radius(5)

print(status)
print(f'Area of circle with radius {x.radius} is {Area}.')
