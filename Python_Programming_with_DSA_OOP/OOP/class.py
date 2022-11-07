# class Person:
#   def __init__(self,person_name):
#     self.person_name = person_name
#   def get_name(self):
#     return self.person_name
# person_1=Person('nahid')
# person_2=Person('niloy')
# print(person_1.get_name())


class Person:
  def __init__(self,person_name,date_of_birth,height):
    self.name = person_name
    self.date_of_birth = date_of_birth
    self.height = height
  
  def info(self):
    print(f"Your name: {self.name}\nYour DOB: {self.date_of_birth}\nYour height: {self.height}")
  
    
      
person_1=Person('nahid',"1995","5.5")
person_1.info()
print(person_1.date_of_birth)
print(person_1.height)





