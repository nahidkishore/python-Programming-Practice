def method_name(a,b):
  print('A method')

class Person:
  def __init__(self, person_name:str,date_of_birth:int,height:int=None):
    self.__name = person_name
    self.__birth_date = date_of_birth
    self.__height = height
    self.abc=None
  def get_year_of_birth(self):
   return self.__birth_date
  
  def get_name(self):
    return self.__name

  def set_name(self,new_name):
    if self.__has_any_number(new_name):
      print("sorry person name can't have number")
      return
    self.name = new_name
    
  def __has_any_number(self,string):
    return "0" in string
  
  def get_summary(self):
    return f'Name: {self.__name}, Birth: {self.__birth_date}, Height: {self.__height}'
    


person_list =[
  Person('nahid','1995',60),
  Person('niloy','2008'),
  Person('Hridoy','1990'),
  Person('jannat','1996',58)

]

for Person in person_list:
  if Person.get_year_of_birth() >= 2000:
    print(a_person.get_summary())

