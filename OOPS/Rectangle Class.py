#defining class
class Rectangle:
    
    #constructor
    def __init__(self,l,b):
        self.length = l;
        self.breadth = b;
        
    #get area
    def area(self):
        return self.length*self.breadth
        
    #get perimeter
    def perimeter(self):
        return 2*(self.length+self.breadth)
    

#creating object
r1 = Rectangle(10,5)
print("Area is : ",r1.area())
print("Perimter is : ",r1.perimeter())
