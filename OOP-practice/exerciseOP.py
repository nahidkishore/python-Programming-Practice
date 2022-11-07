class Triangle:
  
  #constructor
  def __init__(self,base, height):
    self.base=base
    self.height=height
    
    #function
  def calculateArea(self):
    area=0.5*self.base*self.height
    print('Area: ',area)
    
    #object
t1=Triangle(10,20)
t1.calculateArea()

t2=Triangle(20,30)
t2.calculateArea()
