class Rectangle:
    count = 0
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        Rectangle.count += 1
    
    def get_area(self):
        return self.length*self.breadth
    
    def get_perimeter(self):
        return 2*(self.length + self.breadth)
    
    @staticmethod
    def is_square(length, breadth):
        return length == breadth

#static variable
print("Current Rectangle count", Rectangle.count)

rectangle_r1 = Rectangle(10,5)
#static variable
print("Current Rectangle count", Rectangle.count)

rectangle_r2 = Rectangle(8,4)
#static variable
print("Current Rectangle count", Rectangle.count)

print(Rectangle.is_square(10,10))
