class Shape:
  def __init__(self, dim1, dim2):
    self.dim1=dim1
    self.dim2=dim2
  
  def area(self):
    print("this is area method")
    
class Triangle(Shape):
  def area(self):
    area=0.5* self.dim1*self.dim2
    print(area)
    
    
class Rectangle (Shape):
  def area(self):
    area=self.dim1*self.dim2
    print(area)
    
    
t=Triangle(20,30)
t.area()


r=Rectangle(20,30)
r.area()
    