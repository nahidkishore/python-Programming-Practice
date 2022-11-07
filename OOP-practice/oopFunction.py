class Student:
  roll=''
  gpa=''
  
  def display(self):
    print(f"Roll: {self.roll}, GPA: {self.gpa}") #f diye "format bujhaiche"

nahid=Student()
nahid.roll=101
nahid.gpa=3.15
#print('nahid Information')
nahid.display()


naima=Student()
naima.roll=102
naima.gpa=3.5
#print('naima Information')
naima.display()



#Another Easy way to OOP function use

class Student:
  roll=''
  gpa=''
  
  def set_value(self,roll, gpa):
    self.roll=roll
    self.gpa=gpa
    
  
  def display(self):
    print(f"Roll: {self.roll}, GPA: {self.gpa}")
    
niloy=Student()
niloy.set_value(103,3.7)
#print('niloy Information')
niloy.display()


tania=Student()
tania.set_value(105, 3.8)
#print('tania Information')
tania.display()
