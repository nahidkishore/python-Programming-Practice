def method_name(a,b):
  print('A method')

class Person:
  def __init__(self, person_name,date_of_birth,height):
    self.name = person_name
    self.birth_date = date_of_birth
    self.height = height
    
  def get_name(self):
    return self.name
  def set_name(self,new_name):
    self.name = new_name
  
  def get_summary(self):
    return f'Name: {self.name}, Birth: {self.birth_date}, Height: {self.height}'
    
method_name(10,20)
a_person = Person('nahid','1995','5.6 feet')
# b_person = Person('test')

# print(a_person.get_name())
# print(b_person.get_name())
print(a_person.get_summary())
a_person.set_name('nahid islam')
print(a_person.get_summary())
