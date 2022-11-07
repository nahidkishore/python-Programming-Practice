#Example-1
# class Car:
#   def __init__(self):
#     print('init method called')
# car_1=Car()


# #output= init method called

#example-2
# class Car:
#   def __init__(self,name,color):
#     self.name=name
#     self.color=color
# car_1=Car('toyota1', 'green')

# print(car_1.name,car_1.color)

#example-3

class Car:
  def __init__(self,name,color):
    self.name=name
    self.color=color
  def info(self):
    print('this '+self.name+ ' is ' +str(self.color))
  
  def start(self):
    print('started this car')
car_1 = Car('toyota1', 'green')
car_1.info()
car_1.start()


car_2 = Car('toyota2', 'gray')
car_2.info()
car_2.start()