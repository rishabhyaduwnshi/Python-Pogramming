class Cuboid:
    def __init__(self,length,breadth,height):
        self.length = length
        self.breadth = breadth
        self.height = height
        
    def surface_area(self):
        return self.length*self.breadth
        
    def volume(self):
        return self.length*self.breadth*self.height


cuboid_c1 = Cuboid(10,5,3)
print("Area of cuboid_c1 : ", cuboid_c1.surface_area())
    
cuboid_c2 = Cuboid(8,5,4)
print("Volume of cuboid_c2 : ", cuboid_c2.volume())
