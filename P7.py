import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return "C("+str(self.radius+")"

    def circunference(self):
        return 2*math.pi*self.radius

    def area(self):
        return math.pi*self.radius*self.radius

##### Text
circle1 = Circle(10)
print "circle1 radius: ", circle1.radius
