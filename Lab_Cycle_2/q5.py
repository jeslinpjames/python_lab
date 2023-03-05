class threeD_shapes:
    def printVolume(self):
        print("The volume is : ",round(self.volume,3))
    def printArea(self):
        print("The area is : ",self.area)

class Cylinder(threeD_shapes):
    r=None
    h=None
    area=None
    volume=None
    def __init__(self,rad,height):
        self.r=rad
        self.h=height
    def find_area(self):
        self.area=2*3.14*self.r*(self.r+self.h)
    def find_volume(self):
        self.volume=3.14*self.r*self.r*self.h

class Sphere(threeD_shapes):
    r=None
    area=None
    volume=None
    def __init__(self,radius):
        self.r=radius
    def find_area(self):
        self.area=4*3.14*self.r*self.r
    def find_volume(self):
        self.volume=(4/3)*3.14*self.r*self.r*self.r
    
obj1=Cylinder(float(input("Enter the radius of the Cylinder : ")),float(input("Enter the Height of the Cylinder : ")))
obj1.find_area()
obj1.find_volume()
obj1.printArea()
obj1.printVolume()

obj2=Sphere(float(input("Enter the radius of the sphere : ")))
obj2.find_area()
obj2.find_volume()
obj2.printArea()
obj2.printVolume()