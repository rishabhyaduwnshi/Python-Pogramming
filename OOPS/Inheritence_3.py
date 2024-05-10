class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        
    def get_area(self):
        return self.length * self.breadth

#inheriting from Rectangle class
class Cuboid(Rectangle):
    def __init__(self,length,breadth,height):
        self.height = height
        
        #calling the parent class constructor
        super().__init__(length,breadth)
    
    def get_volume(self):
        return self.length * self.breadth * self.height
    


cuboid_c1 = Cuboid(10,8,5)
print(cuboid_c1.get_volume())
