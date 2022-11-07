#abstract method use kora hoy, 1ta model hisabe use korar jonno, and sobai jeno iccha moto reuse korte pare

from abc import ABC, abstractmethod

class Shape(ABC):
  def __init__(self, dim1, dim2):
    self.dim1=dim1
    self.dim2=dim2
  @abstractmethod
  
  
  def area(self):
    pass
    
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
    