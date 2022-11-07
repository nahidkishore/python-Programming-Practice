class Person:
  def __init__(self,person_name:str,date_of_birth:int,height):
    self.name = person_name
    self.date_of_birth = date_of_birth
    self.height = height
  # def get_name(self):
  #   return self.name
  # def get_date_of_birth(self):
  #   return self.date_of_birth
  
  def info(self):
    print(f"Your name: {self.name}\nYour DOB: {self.date_of_birth}\nYour height: {self.height}")
  
    
      
# person_1=Person('nahid',"1995","5.5")
# person_1.info()
# print(person_1.date_of_birth)
# print(person_1.height)


# inheritance

class Student(Person):
  def __init__(self,person_name:str,date_of_birth:int, email_id:str,student_id:str):
    super().__init__(person_name,date_of_birth)
    self.id=student_id
    self.email=email_id
  
  def info(self):
    return f"Name: {self.get_name()} Email:{self.email} Birth:{self.get_date_of_birth()}"
  
  
student=Student("A",2000,"a@gmail.com","123123test")

print(student.info())
    




